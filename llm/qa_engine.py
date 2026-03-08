from llm.llm_client import LLMClient


class QAEngine:

    def __init__(self):
        self.llm = LLMClient()

    def ask(self, context, question):

        dataset_summary = (
            f"Dataset Information:\n"
            f"Rows: {context.rows}\n"
            f"Columns: {context.columns}\n\n"
            f"Column Names: {', '.join(context.column_names)}\n\n"
            f"Numeric Features: {', '.join(context.numeric_features)}\n"
            f"Categorical Features: {', '.join(context.categorical_features)}\n"
        )

        prompt = (
            "You are a helpful data analyst.\n\n"
            "Use the dataset information below to answer the user's question.\n\n"
            f"{dataset_summary}\n"
            f"Question: {question}\n"
            "Answer clearly."
        )

        answer = self.llm.generate(prompt)

        return answer
