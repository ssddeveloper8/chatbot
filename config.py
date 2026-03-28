MODEL_NAME = "mistral"
OLLAMA_URL = "http://localhost:11434/api/generate"

EMBED_MODEL = "all-MiniLM-L6-v2"

MAX_ROWS = 100
TOP_K_TABLES = 5

DB_DESCRIPTIONS = {
    "builder": "contains user data, configuration, KPI definitions,TAG definitions, All configuration, tables like tbl_mst_user, tbl_kpi_engine_kpi_calculation, department data, user info",
    "historian": "contains KPI values, performance data, time series data, tag values, sensor data, tables like tbl_current_kpi_historian_data, KPI performance, time series, tag data"
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