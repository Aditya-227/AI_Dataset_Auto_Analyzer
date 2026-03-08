import os


class LLMClient:

    def __init__(self):

        self.groq_key = os.getenv("GROQ_API_KEY")

        if self.groq_key:
            from groq import Groq
            self.mode = "groq"
            self.client = Groq(api_key=self.groq_key)

        else:
            import ollama
            self.mode = "ollama"
            self.client = ollama

    def generate(self, prompt):

        if self.mode == "groq":

            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )

            return response.choices[0].message.content

        else:

            response = self.client.chat(
                model="llama3",
                messages=[{"role": "user", "content": prompt}]
            )

            return response["message"]["content"]