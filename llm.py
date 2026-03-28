import requests
from config import OLLAMA_URL, MODEL_NAME
from utils import clean_sql


def extract_entity(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]

def generate_sql(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    raw_output = response.json()["response"]

    print("\n RAW LLM OUTPUT:\n", raw_output)

    sql = clean_sql(raw_output)

    print("\n CLEAN SQL:\n", sql)

    return sql