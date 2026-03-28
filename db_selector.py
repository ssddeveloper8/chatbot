from embeddings import embed, cosine
from config import DB_DESCRIPTIONS


def select_database(user_query):
    query_emb = embed(user_query)

    best_db = None
    best_score = -1

    for db, desc in DB_DESCRIPTIONS.items():
        db_emb = embed(desc)
        score = cosine(query_emb, db_emb)

        if score > best_score:
            best_score = score
            best_db = db

    print(f"DB Selected: {best_db} (score={best_score:.3f})")

    return best_db