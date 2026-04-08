from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from schema_loader import extract_schema, format_schema
from table_selector import select_tables, build_table_embeddings
from prompt_builder import build_prompt
from llm import generate_sql
from validator import validate_sql
from executor import execute_sql
from utils import normalize_text
from db_selector import select_database
from database import init_pools

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_pools()

schemas = {
    "builder": extract_schema("builder"),
    "historian": extract_schema("historian")
}

for schema in schemas.values():
    build_table_embeddings(schema)

CACHE = {}

@app.post("/ask")
async def ask_api(request: Request):
    body = await request.body()
    user_query = normalize_text(body.decode("utf-8"))

    if user_query in CACHE:
        return CACHE[user_query]

    db = select_database(user_query)
    schema = schemas[db]
    tables = select_tables(user_query)
    schema_text = format_schema(schema, tables)
    prompt = build_prompt(user_query, schema_text)
    sql = generate_sql(prompt)

    valid, err = validate_sql(sql, schema)
    if not valid:
        return {"error": err, "sql": sql}

    data = execute_sql(db, sql)

    result = {
        "query": user_query,
        "database": db,
        "sql": sql,
        "data": data
    }

    CACHE[user_query] = result
    return result

@app.get("/health")
async def health_check():
    return {"status": "ok"}