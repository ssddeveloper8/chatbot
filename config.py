import os

# LLM Config
MODEL_NAME = os.getenv("MODEL_NAME", "mistral")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434/api/generate")

# Embedding Model
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

# Limits
MAX_ROWS = int(os.getenv("MAX_ROWS", 100))
TOP_K_TABLES = int(os.getenv("TOP_K_TABLES", 5))

# DB Descriptions
DB_DESCRIPTIONS = {
    "builder": "contains user data, configuration, KPI definitions, TAG definitions, tables like tbl_mst_user, tbl_kpi_engine_kpi_calculation, department data",
    "historian": "contains KPI values, performance data, time series data, tag values, sensor data, tables like tbl_current_kpi_historian_data"
}

# Databases
DATABASES = {
    "builder": {
        "host": os.getenv("BUILDER_DB_HOST", "host.docker.internal"),
        "port": 5432,
        "database": os.getenv("BUILDER_DB_NAME"),
        "user": os.getenv("BUILDER_DB_USER"),
        "password": os.getenv("BUILDER_DB_PASSWORD")
    },
    "historian": {
        "host": os.getenv("HISTORIAN_DB_HOST", "host.docker.internal"),
        "port": int(os.getenv("HISTORIAN_DB_PORT")),
        "database": os.getenv("HISTORIAN_DB_NAME"),
        "user": os.getenv("HISTORIAN_DB_USER"),
        "password": os.getenv("HISTORIAN_DB_PASSWORD")
    }
}