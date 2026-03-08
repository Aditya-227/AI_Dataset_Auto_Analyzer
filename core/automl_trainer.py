from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, r2_score
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC


class AutoMLTrainer:

    def preprocess(self, df, target):

        df = df.copy()

        # drop obvious id columns
        id_cols = [c for c in df.columns if "id" in c.lower()]
        df = df.drop(columns=id_cols, errors="ignore")

        y = df[target]
        X = df.drop(columns=[target])

        # drop high-cardinality columns
        high_cardinality = ["Ticket", "Cabin", "Name"]

        X = X.drop(columns=high_cardinality, errors="ignore")

        # fill numeric missing values
        num_cols = X.select_dtypes(include=["number"]).columns
        X[num_cols] = X[num_cols].fillna(X[num_cols].median())

        # encode categorical columns
        cat_cols = X.select_dtypes(include=["object", "category"]).columns
        X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

        return X, y

    def train(self, context):

        target = context.patterns.get("potential_target")

        if not target:
            return None

        df = context.dataframe

        X, y = self.preprocess(df, target)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # detect classification vs regression
        unique_values = y.nunique()

        if unique_values <= 20:

            models = {
                "Logistic Regression": LogisticRegression(max_iter=200),
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "SVM": SVC()
            }

            results = {}

            best_model = None
            best_score = 0

            for name, m in models.items():

                m.fit(X_train, y_train)
                preds = m.predict(X_test)

                acc = accuracy_score(y_test, preds)

                results[name] = acc

                if acc > best_score:
                    best_score = acc
                    best_model = m

            model = best_model
            score = best_score

        else:
            # regression problem
            model = RandomForestRegressor()
            model.fit(X_train, y_train)

            preds = model.predict(X_test)
            score = r2_score(y_test, preds)

        # compute feature importance only if supported
        importance = None

        if hasattr(model, "feature_importances_"):

            importance = pd.Series(
                model.feature_importances_,
                index=X.columns
            ).sort_values(ascending=False)

            # group encoded features
            importance.index = importance.index.str.split("_").str[0]
            importance = importance.groupby(importance.index).sum().sort_values(ascending=False)

        return {
            "model": model,
            "score": score,
            "importance": importance,
            "model_results": results if unique_values <= 20 else None
        }