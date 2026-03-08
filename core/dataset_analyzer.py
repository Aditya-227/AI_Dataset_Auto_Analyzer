import pandas as pd
from core.context import DatasetContext


class DatasetAnalyzer:

    def analyze(self, context: DatasetContext) -> DatasetContext:

        df = context.dataframe

        # detect numeric columns
        context.numeric_features = df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        # detect categorical columns
        context.categorical_features = df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        # detect datetime columns
        context.datetime_features = df.select_dtypes(
            include=["datetime64"]
        ).columns.tolist()

        # missing values
        missing = df.isnull().sum()
        context.missing_values = missing[missing > 0].to_dict()

        # correlations
        if len(context.numeric_features) > 1:
            context.correlations = df[context.numeric_features].corr()

        return context