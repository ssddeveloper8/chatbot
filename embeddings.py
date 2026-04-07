from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBED_MODEL, DB_DESCRIPTIONS

model = SentenceTransformer(EMBED_MODEL)

# Cache DB embeddings
DB_EMBEDDINGS = {
    db: model.encode(desc)
    for db, desc in DB_DESCRIPTIONS.items()
}

def embed(text):
    return model.encode(text)

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))