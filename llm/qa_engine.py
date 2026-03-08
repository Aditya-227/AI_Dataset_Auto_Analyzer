from llm.llm_client import LLMClient


class QAEngine:

    def __init__(self):
        self.llm = LLMClient()

    def ask(self, context, question):

        # simple questions handled locally
        q = question.lower()

        if "rows" in q:
            return f"The dataset contains {context.rows} rows."

        if "columns" in q:
            return f"The dataset contains {context.columns} columns."

        summary = f"""
Rows: {context.rows}
Columns: {context.columns}
Columns list: {', '.join(map(str, context.column_names[:10]))}
"""

        prompt = f"""
Dataset summary:
{summary}

Question: {question}
"""

        return self.llm.generate(prompt)
