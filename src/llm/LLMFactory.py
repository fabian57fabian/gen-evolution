from enum import Enum
from typing import Callable

from .AbstractLLM import AbstractLLM


class LLMType(Enum):
    gpt = 0,
    cohere = 1,
    groq = 2


class LLMFactory:

    def build_llm(self, type: str or LLMType) -> AbstractLLM:
        """
        Builds an llm class based on type e.g. "cohere" or LLMType.gpt.
        """
        llm_type = self.__parse_enum(type)
        if llm_type == LLMType.cohere:
            from .CohereLLM import CohereLLM
            return CohereLLM()
        if llm_type == LLMType.gpt:
            from .OpenAILLM import OpenAILLM
            return OpenAILLM()
        if llm_type == LLMType.groq:
            from .GroqLLM import GroqLLM
            return GroqLLM()
        raise "Not implemented"

    def __parse_enum(self, value: str or LLMType) -> LLMType:
        if isinstance(value, str):
            try:
                return LLMType(value)
            except ValueError:
                raise ValueError(f"Invalid LLMType value: {value}")
        elif isinstance(value, LLMType):
            return value
        else:
            raise TypeError("Value must be a string or a LLMType")
