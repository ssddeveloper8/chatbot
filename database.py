import psycopg2
from config import DATABASES

def get_connection(db_name):
    cfg = DATABASES[db_name]
    return psycopg2.connect(**cfg)