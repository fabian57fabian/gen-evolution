from .AbstractLLM import AbstractLLM

import cohere


class CohereLLM(AbstractLLM):
    def __init__(self):
        allowed_models = ["command-r"]
        super().__init__(allowed_models, "command-r")

    def ask(self, messages: list, temperature: float = 0.7):
        # Needs CO_API_KEY env var
        co = cohere.ClientV2()
        response = co.chat(
            model=self.model,
            messages=messages,
            temperature=temperature
        )
        return response.message.content[0].text
