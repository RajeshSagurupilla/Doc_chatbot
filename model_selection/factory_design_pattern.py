from model_selection.base_model import BaseModel
from model_selection.openai import OpenAIModel
# from model_selection.huggingface_model import HuggingFaceModel
from model_selection.mixtral import MistralModel

class ModelFactory:
    @staticmethod
    def get_model(model_name: str) -> BaseModel:
        model_name = model_name.lower()
        if model_name == "openai":
            return OpenAIModel()
        elif model_name == "huggingface":
            pass
        elif model_name == "mixtral":
            return MistralModel()
        else:
            raise ValueError(f"Unknown model: {model_name}")
