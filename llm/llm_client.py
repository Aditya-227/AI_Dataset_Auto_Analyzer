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

        try:

            if self.mode == "groq":

                response = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a helpful data analyst."},
                        {"role": "user", "content": str(prompt)}
                    ],
                    temperature=0.2,
                    max_tokens=300
                )

                return response.choices[0].message.content

            else:

                response = self.client.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": str(prompt)}]
                )

                return response["message"]["content"]

        except Exception as e:

            # prevent app crash
            return f"LLM error occurred: {str(e)}"
