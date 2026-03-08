import pandas as pd
from core.context import DatasetContext


class PatternDetector:

    def detect(self, context: DatasetContext) -> DatasetContext:

        df = context.dataframe
        patterns = {}

        # HIGH CORRELATION DETECTION
        high_corr = []

        if context.correlations is not None:

            corr_matrix = context.correlations

            for col1 in corr_matrix.columns:
                for col2 in corr_matrix.columns:

                    if col1 != col2:
                        value = corr_matrix.loc[col1, col2]

                        if abs(value) > 0.8:
                            high_corr.append((col1, col2, value))

        patterns["high_correlations"] = high_corr

        # POTENTIAL TARGET DETECTION
        potential_target = None

        for col in context.categorical_features:

            unique_vals = df[col].nunique()

            if 2 <= unique_vals <= 20:
                potential_target = col
                break

        patterns["potential_target"] = potential_target

        # CLASS IMBALANCE CHECK
        imbalance = None

        if potential_target:

            counts = df[potential_target].value_counts(normalize=True)

            if counts.max() > 0.8:
                imbalance = True
            else:
                imbalance = False

        patterns["class_imbalance"] = imbalance

        context.patterns = patterns

        return context