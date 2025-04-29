import openai
from model_selection.factory_design_pattern import BaseModel


class OpenAIModel(BaseModel):
    def generate_answer(self,prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()