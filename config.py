MODEL_NAME = "mistral"
OLLAMA_URL = "http://localhost:11434/api/generate"

EMBED_MODEL = "all-MiniLM-L6-v2"

MAX_ROWS = 100
TOP_K_TABLES = 5

DB_DESCRIPTIONS = {
    "builder": "contains user data, KPI definitions, tag definitions, config tables",
    "historian": "contains KPI values, time series data, tag values, sensor data"
}

DATABASES = {
    "builder": {
        "host": "localhost",
        "port": 5432,
        "database": "Builder DB",
        "user": "postgres",
        "password": "root"
    },
    "historian": {
        "host": "localhost",
        "port": 5432,
        "database": "Historian DB",
        "user": "postgres",
        "password": "root"
    }
}