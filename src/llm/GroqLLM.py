from .AbstractLLM import AbstractLLM

import groq


class GroqLLM(AbstractLLM):
    def __init__(self):
        allowed_models = ["gemma-7b-it", "llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]
        super().__init__(allowed_models, "gemma-7b-it")

    def ask(self, messages: list, temperature: float = 0.7):
        # Needs GROQ_API_KEY env var
        client = groq.Client()
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=temperature
        )
        return chat_completion.choices[0].message.content
