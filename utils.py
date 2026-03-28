import re


def clean_sql(response: str):
    import re

    if not response:
        return ""

    response = response.replace("```sql", "").replace("```", "").strip()

    response = response.replace("\n", " ")

    response = re.sub(r"\s+", " ", response)

    match = re.search(r"(SELECT .*?;)", response, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return response.strip()


def normalize_text(text: str):
    """
    Normalize user query
    """
    return text.strip().lower()


def is_select_query(sql: str):
    """
    Check if query is SELECT
    """
    return sql.strip().lower().startswith("select")


def contains_forbidden(sql: str):
    """
    Check unsafe SQL keywords
    """
    forbidden = ["drop", "delete", "update", "insert", "alter"]

    sql = sql.lower()
    return any(word in sql for word in forbidden)