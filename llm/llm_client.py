import os
import streamlit as st


class LLMClient:

    def __init__(self):

        # Read API key from Streamlit secrets first
        self.groq_key = None

        try:
            self.groq_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            self.groq_key = os.getenv("GROQ_API_KEY")

        if self.groq_key:
            from groq import Groq
            self.mode = "groq"
            self.client = Groq(api_key=self.groq_key)
        else:
            self.mode = "none"
            self.client = None

        print("LLM MODE:", self.mode)

    def generate(self, prompt):

        if self.mode != "groq":
            return "LLM not configured."

        try:

            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful data analyst."
                    },
                    {
                        "role": "user",
                        "content": str(prompt)
                    }
                ],
                max_tokens=300
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"LLM request failed: {str(e)}"
