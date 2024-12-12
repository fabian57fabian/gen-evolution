from abc import ABC, abstractmethod


class AbstractLLM(ABC):
    def __init__(self, models: list, model=""):
        self.models = models
        self.model = model

    def set_model(self, model: str):
        print(f"Setting model {model}")
        self.model = model

    @abstractmethod
    def ask(self, messages: list, temperature: float = 0.7):
        pass
