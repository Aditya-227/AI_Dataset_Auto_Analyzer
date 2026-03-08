from llm.llm_client import LLMClient
from llm.prompt_builder import PromptBuilder


class QAEngine:

    def __init__(self):
        from llm.llm_client import LLMClient
        self.llm = LLMClient()

    def ask(self, context, question):

        # build lightweight context instead of sending full dataframe
        dataset_summary = f"""
Dataset information:
Rows: {context.rows}
Columns: {context.columns}

Column names:
{", ".join(context.column_names)}

Numeric features:
{", ".join(context.numeric_features)}

Categorical features:
{", ".join(context.categorical_features)}
"""

        prompt = f"""
You are a data analyst assistant.

Use the dataset information below to answer the question.

{dataset_summary}

Question: {question}
Answer concisely.
"""

        answer = self.llm.generate(prompt)

        return answer
