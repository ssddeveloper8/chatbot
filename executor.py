from database import get_connection

def execute_sql(db_name, sql):
    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()

    cols = [desc[0] for desc in cursor.description]

    cursor.close()
    conn.close()

    return [dict(zip(cols, r)) for r in rows]