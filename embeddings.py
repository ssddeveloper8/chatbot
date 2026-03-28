from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBED_MODEL

model = SentenceTransformer(EMBED_MODEL)

def embed(text):
    return model.encode(text)

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))