from llm.llm_client import LLMClient


class QAEngine:

    def __init__(self):
        self.llm = LLMClient()

    def ask(self, context, question):

        numeric = ", ".join(map(str, context.numeric_features))
        categorical = ", ".join(map(str, context.categorical_features))
        columns = ", ".join(map(str, context.column_names))

        dataset_summary = (
            f"Dataset Information:\n"
            f"Rows: {context.rows}\n"
            f"Columns: {context.columns}\n\n"
            f"Column Names: {columns}\n\n"
            f"Numeric Features: {numeric}\n"
            f"Categorical Features: {categorical}\n"
        )

        prompt = (
            "You are a helpful data analyst.\n\n"
            "Use the dataset information below to answer the question.\n\n"
            f"{dataset_summary}\n"
            f"Question: {question}\n"
            "Answer concisely."
        )

        return self.llm.generate(prompt)
