import psycopg2
from config import DATABASES


def get_connections():
    conns = {}

    for name, cfg in DATABASES.items():
        try:
            conns[name] = psycopg2.connect(
                host=cfg["host"],
                dbname=cfg["database"],
                user=cfg["user"],
                password=cfg["password"],
                port=cfg["port"]
            )
            print(f"{name} DB connected ✅")

        except Exception as e:
            print(f"{name} DB connection failed ❌:", str(e))
            conns[name] = None

    return conns