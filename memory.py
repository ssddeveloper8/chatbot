from database import get_connection

def save_memory(query, sql, db, success, confidence):
    conn = get_connection("builder")  # store centrally
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO query_memory (user_query, generated_sql, database_name, success, confidence)
        VALUES (%s, %s, %s, %s, %s)
    """, (query, sql, db, success, confidence))

    conn.commit()
    cur.close()
    conn.close()