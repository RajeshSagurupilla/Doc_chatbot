import requests
from configurations.config import *
from model_selection.factory_design_pattern import BaseModel

class MistralModel(BaseModel):
    def generate_answer(self,prompt):
        headers = {
            "Authorization": f"Bearer {MIXTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mixtral-8x7b",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(MIXTRAL_API_URL, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"].strip()