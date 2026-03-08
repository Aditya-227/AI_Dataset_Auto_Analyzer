from llm.llm_client import LLMClient


class QAEngine:

    def __init__(self):
        self.llm = LLMClient()

    def ask(self, context, question):

        q = question.lower()

        # answer simple questions locally
        if "rows" in q:
            return f"The dataset contains {context.rows} rows."

        if "columns" in q:
            return f"The dataset contains {context.columns} columns."

        prompt = f"""
Dataset summary:
Rows: {context.rows}
Columns: {context.columns}

Question: {question}
"""

        return self.llm.generate(prompt)
