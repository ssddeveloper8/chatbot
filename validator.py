from utils import is_select_query, contains_forbidden


def validate_sql(sql, schema):
    sql_clean = sql.strip()

    if not is_select_query(sql_clean):
        return False, f"Invalid SQL generated: {sql}"

    if contains_forbidden(sql_clean):
        return False, "Unsafe query detected"

    return True, ""