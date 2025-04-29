from pydantic import BaseModel

class PromptResponse(BaseModel):
    prompt:str
    model_name:str