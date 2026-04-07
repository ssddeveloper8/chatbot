from embeddings import embed, cosine
from config import TOP_K_TABLES

TABLE_EMBEDDINGS = {}

def build_table_embeddings(schema):
    for table, cols in schema.items():
        text = table + " " + " ".join([c['column'] for c in cols])
        TABLE_EMBEDDINGS[table] = embed(text)

def select_tables(query):
    q_emb = embed(query)

    scores = []
    for table, t_emb in TABLE_EMBEDDINGS.items():
        score = cosine(q_emb, t_emb)
        scores.append((table, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [t[0] for t in scores[:TOP_K_TABLES]]