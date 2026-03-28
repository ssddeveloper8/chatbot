from llm import extract_entity
import json


def get_entity_info(user_query):
    prompt = f"""
Extract entity information from user query.

Return JSON ONLY like:
{{
  "type": "kpi/tag/none",
  "value": "entity name"
}}

Query:
{user_query}
"""

    response = extract_entity(prompt)

    try:
        return json.loads(response)
    except:
        return {"type": "none", "value": None}