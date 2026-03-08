from llm.llm_client import LLMClient
from llm.prompt_builder import PromptBuilder


class InsightEngine:

    def __init__(self):
        self.llm = LLMClient()
        self.prompt_builder = PromptBuilder()

    def generate_insights(self, context):

        prompt = f"""
You are a senior data scientist.

Analyze the dataset summary and provide insights.

Dataset Summary

Rows: {context.rows}
Columns: {context.columns}

Numeric Features:
{context.numeric_features}

Categorical Features:
{context.categorical_features}

Missing Values:
{context.missing_values}

Patterns:
{context.patterns}

Provide:

1. Key dataset observations
2. Potential ML problem type
3. Data preprocessing suggestions
4. Model recommendations
5. Possible risks in the dataset
"""

        response = self.llm.generate(prompt)

        return response