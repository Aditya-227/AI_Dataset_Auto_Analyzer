from core.context import DatasetContext


class MLRecommender:

    def recommend_problem_type(self, context: DatasetContext):

        target = context.patterns.get("potential_target")

        if target:

            if target in context.categorical_features:
                return "Classification"

            if target in context.numeric_features:
                return "Regression"

        return "Clustering / Unsupervised"

    def recommend_models(self, context: DatasetContext):

        problem_type = self.recommend_problem_type(context)

        if problem_type == "Classification":

            return [
                "Logistic Regression",
                "Random Forest Classifier",
                "Gradient Boosting",
                "Support Vector Machine"
            ]

        if problem_type == "Regression":

            return [
                "Linear Regression",
                "Random Forest Regressor",
                "Gradient Boosting Regressor",
                "SVR"
            ]

        return [
            "K-Means Clustering",
            "DBSCAN",
            "Hierarchical Clustering"
        ]

    def generate_recommendations(self, context: DatasetContext):

        problem_type = self.recommend_problem_type(context)
        models = self.recommend_models(context)

        context.recommended_models = models

        return {
            "problem_type": problem_type,
            "models": models
        }