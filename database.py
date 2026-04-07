from psycopg2.pool import SimpleConnectionPool
from config import DATABASES

pools = {}

def init_pools():
    for db_name, cfg in DATABASES.items():
        pools[db_name] = SimpleConnectionPool(
            1, 10, **cfg
        )

def get_connection(db_name):
    return pools[db_name].getconn()

def release_connection(db_name, conn):
    pools[db_name].putconn(conn)