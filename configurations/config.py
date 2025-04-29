import os

# Direct access
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","YOUR_API_KEY")
MIXTRAL_API_KEY = os.getenv("MIXTRAL_API_KEY",'YOUR_API_KEY')
MIXTRAL_API_URL = os.getenv("MIXTRAL_API_URL","https://router.huggingface.co/hf-inference/models/mistralai/Mixtral-8x7B-Instruct-v0.1/v1/chat/completions")
