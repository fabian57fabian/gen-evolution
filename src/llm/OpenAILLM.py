from .AbstractLLM import AbstractLLM
from openai import OpenAI


class OpenAILLM(AbstractLLM):
    def __init__(self):
        allowed_models = ["gpt-4o-mini"]
        super().__init__(allowed_models, "gpt-4o-mini")

    def ask(self, messages: list, temperature: float = 0.7):
        # Needs OPENAI_API_KEY env var
        client = OpenAI()
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=temperature
        )
        return chat_completion.choices[0].message.content
