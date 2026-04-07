from database import get_connection, release_connection

def execute_sql(db_name, sql):
    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    cols = [desc[0] for desc in cursor.description]

    cursor.close()
    release_connection(db_name, conn)

    return [dict(zip(cols, r)) for r in rows]