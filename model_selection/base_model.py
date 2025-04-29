from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def generate_answer(self, prompt: str) -> str:
        pass
