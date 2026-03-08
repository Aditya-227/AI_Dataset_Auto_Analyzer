from llm.llm_client import LLMClient
from llm.prompt_builder import PromptBuilder


class QAEngine:

    def __init__(self):

        self.llm = LLMClient()
        self.prompt_builder = PromptBuilder()

    def ask(self, context, question):

        prompt = self.prompt_builder.build_prompt(context, question)

        answer = self.llm.generate(prompt)

        return answer