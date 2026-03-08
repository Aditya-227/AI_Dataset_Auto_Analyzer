import pandas as pd
from core.context import DatasetContext


class DatasetLoader:

    def load_dataset(self, file):

        context = DatasetContext()

        filename = file.name.lower()

        if filename.endswith(".csv"):
            df = pd.read_csv(file)

        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file)

        else:
            raise ValueError("Unsupported file type")

        # clean numeric columns containing commas
        for col in df.columns:

            if df[col].dtype == "object":

                cleaned = (
                    df[col]
                    .astype(str)
                    .str.replace(",", "", regex=False)
                )

                converted = pd.to_numeric(cleaned, errors="ignore")

                df[col] = converted

        context.dataframe = df
        context.rows = df.shape[0]
        context.columns = df.shape[1]
        context.column_names = list(df.columns)

        return context