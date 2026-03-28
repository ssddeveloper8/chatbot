from embeddings import embed, cosine
from config import TOP_K_TABLES

def select_tables(query, schema):
    q_emb = embed(query)
    scores = []

    for table, cols in schema.items():
        text = table + " " + " ".join([c['column'] for c in cols])
        t_emb = embed(text)
        score = cosine(q_emb, t_emb)
        scores.append((table, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [t[0] for t in scores[:TOP_K_TABLES]]