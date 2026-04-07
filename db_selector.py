from embeddings import embed, cosine, DB_EMBEDDINGS

def select_database(user_query):
    query_emb = embed(user_query)

    best_db, best_score = None, -1

    for db, db_emb in DB_EMBEDDINGS.items():
        score = cosine(query_emb, db_emb)

        if score > best_score:
            best_score = score
            best_db = db

    return best_db