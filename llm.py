import requests
from config import OLLAMA_URL, MODEL_NAME
from utils import clean_sql

def generate_sql(prompt):
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        response.raise_for_status()
        data = response.json()

        if "response" not in data:
            raise ValueError(f"Invalid response from LLM: {data}")

        return clean_sql(data["response"])

    except Exception as e:
        print("LLM ERROR:", str(e))
        return "ERROR: Failed to generate SQL"