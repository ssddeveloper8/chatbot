import requests
from config import OLLAMA_URL, MODEL_NAME
from utils import clean_sql

def generate_sql(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    output = response.json()["response"]
    return clean_sql(output)