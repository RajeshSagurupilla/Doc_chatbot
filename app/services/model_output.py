from prompt.base import Prompt_Template
from model_selection.factory_design_pattern import ModelFactory
model_selection = ModelFactory()

def model_output(*args):
    prompt = args[0]
    text = args[1]
    model_name=args[2]
    prompt_temp = Prompt_Template.format(text=text,prompt=prompt)
    model_res = model_selection.get_model(model_name)
    llm_response = model_res.generate_answer(prompt_temp)
    return llm_response
    


