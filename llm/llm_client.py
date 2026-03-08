import os
import streamlit as st


class LLMClient:

    def __init__(self):

        self.groq_key = None

        # Try Streamlit secrets first
        try:
            self.groq_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            self.groq_key = os.getenv("GROQ_API_KEY")

        if self.groq_key:
            from groq import Groq
            self.mode = "groq"
            self.client = Groq(api_key=self.groq_key)

        else:
            try:
                import ollama
                self.mode = "ollama"
                self.client = ollama
            except Exception:
                self.mode = "none"
                self.client = None

        print("LLM MODE:", self.mode)

    def generate(self, prompt):

        try:

            if self.mode == "groq":

                response = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a helpful data analyst."},
                        {"role": "user", "content": str(prompt)}
                    ],
                    max_tokens=300
                )

                return response.choices[0].message.content

            elif self.mode == "ollama":

                response = self.client.chat(
                    model="llama3",
                    messages=[{"role": "user", "content": str(prompt)}]
                )

                return response["message"]["content"]

            else:
                return "LLM not configured."

        except Exception as e:
            return f"LLM request failed: {str(e)}"
