import faiss
import numpy as np
from rag.embedding import kb_embeddings
from kb.snippet import snippet

dimension = kb_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(kb_embeddings)

def store() -> tuple:
    return index, snippet