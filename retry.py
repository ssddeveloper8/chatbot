from llm import generate_sql

def retry_sql(query, error, schema_text):
    prompt = f"""
The SQL failed.

ERROR:
{error}

Fix the SQL.

STRICT RULES:
- Use ONLY tables from the given schema
- Do NOT join tables from different databases
- Fix column names correctly
- Prefer simple SELECT query
- Return ONLY SQL

SCHEMA:
{schema_text}

USER QUERY:
{query}

Correct SQL:
"""
    return generate_sql(prompt)