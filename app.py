from fastapi import FastAPI, Request

from schema_loader import extract_schema, format_schema
from table_selector import select_tables
from prompt_builder import build_prompt
from llm import generate_sql
from validator import validate_sql
from executor import execute_sql
from retry import retry_sql
from utils import normalize_text

from entity_extractor import get_entity_info
from entity_resolver import resolve_entity

from db_selector import select_database

app = FastAPI()

# Load schemas once
schemas = {
    "builder": extract_schema("builder"),
    "historian": extract_schema("historian")
}


@app.post("/ask")
async def ask_api(request: Request):

    body = await request.body()
    user_query = normalize_text(body.decode("utf-8"))

    print("\n USER QUERY:", user_query)

    entity = get_entity_info(user_query)
    print("ENTITY DETECTED:", entity)

    if entity.get("type") in ["kpi", "tag"]:

        resolved = resolve_entity(entity["type"], entity["value"])
        print("RESOLVED ENTITY:", resolved)

        if not resolved:
            return {"error": f"{entity['type']} not found"}

        try:

            if entity["type"] == "kpi":
                sql = f"""
                SELECT AVG(value) as avg_value
                FROM tbl_current_kpi_historian_data
                WHERE alise = '{resolved['alias']}';
                """
                db = "historian"


            elif entity["type"] == "tag":
                sql = f"""
                SELECT AVG(value) as avg_value
                FROM tbl_current_tag_historian_data
                WHERE tag_id = '{resolved['tag_id']}';
                """
                db = "historian"

            print("FINAL ENTITY SQL:", sql)

            data = execute_sql(db, sql)

            return {
                "query": user_query,
                "entity": entity,
                "resolved": resolved,
                "sql": sql,
                "data": data
            }

        except Exception as e:
            return {
                "error": "Entity-based execution failed",
                "details": str(e)
            }


    db = select_database(user_query)
    print("DB SELECTED:", db)

    schema = schemas[db]

    tables = select_tables(user_query, schema)
    print("SELECTED TABLES:", tables)

    schema_text = format_schema(schema, tables)

    prompt = build_prompt(user_query, schema_text, "")


    sql = generate_sql(prompt)
    print("GENERATED SQL:", sql)


    valid, err = validate_sql(sql, schema)

    if not valid:
        return {"error": err, "sql": sql}


    try:
        data = execute_sql(db, sql)

    except Exception as e:
        print("FIRST ERROR:", str(e))

        try:
            fixed_sql = retry_sql(user_query, str(e), schema_text)
            print("🔁 RETRY SQL:", fixed_sql)

            data = execute_sql(db, fixed_sql)
            sql = fixed_sql

        except Exception as e2:
            return {
                "error": "Execution failed",
                "details": str(e2),
                "original_sql": sql
            }

    return {
        "query": user_query,
        "database": db,
        # "tables_used": tables,
        "sql": sql,
        "data": data
    }
