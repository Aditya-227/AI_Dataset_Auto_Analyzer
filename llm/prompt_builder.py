from core.context import DatasetContext


class PromptBuilder:

    def build_prompt(self, context: DatasetContext, question: str):

        summary = f"""
Dataset Summary

Rows: {context.rows}
Columns: {context.columns}

Numeric Features: {context.numeric_features}

Categorical Features: {context.categorical_features}

Missing Values: {context.missing_values}

Patterns Detected: {context.patterns}

Answer the user question using this dataset information.
"""

        return summary + "\nUser Question:\n" + question