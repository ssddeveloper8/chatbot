import os


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"  
)

MODEL_NAME = os.getenv("MODEL_NAME", "mistral")


# Embedding Model
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")

# Limits
MAX_ROWS = int(os.getenv("MAX_ROWS", 100))
TOP_K_TABLES = int(os.getenv("TOP_K_TABLES", 5))

# DB Descriptions
DB_DESCRIPTIONS = {
    "builder": "contains user data, configuration, KPI definitions, TAG definitions",
    "historian": "contains KPI values, performance data, time series data"
}

# Databases
DATABASES = {
    "builder": {
        "host": os.getenv("BUILDER_DB_HOST", "host.docker.internal"),
        "port": int(os.getenv("BUILDER_DB_PORT", 5432)),
        "database": os.getenv("BUILDER_DB_NAME", "Builder_DB"),
        "user": os.getenv("BUILDER_DB_USER", "postgres"),
        "password": os.getenv("BUILDER_DB_PASSWORD", "admin")
    },
    "historian": {
        "host": os.getenv("HISTORIAN_DB_HOST", "host.docker.internal"),
        "port": int(os.getenv("HISTORIAN_DB_PORT", 5432)),   # ✅ FIXED
        "database": os.getenv("HISTORIAN_DB_NAME", "Historian_DB"),
        "user": os.getenv("HISTORIAN_DB_USER", "postgres"),
        "password": os.getenv("HISTORIAN_DB_PASSWORD", "admin")
    }
}