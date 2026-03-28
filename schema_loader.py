from collections import defaultdict
from database import get_connection

def extract_schema(db_name):
    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT table_name, column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    rows = cursor.fetchall()
    schema = defaultdict(list)

    for table, col, dtype in rows:
        schema[table].append({"column": col, "type": dtype})

    cursor.close()
    conn.close()

    return dict(schema)


def format_schema(schema, selected_tables):
    text = ""
    for table in selected_tables:
        if table in schema:
            text += f"\nTable: {table}\n"
            for col in schema[table]:
                text += f" - {col['column']} ({col['type']})\n"
    return text