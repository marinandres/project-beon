import numpy as np
from rag.embedding import model
from rag.vector_store import store

def retrieve(question: str, top_k: int = 1) -> str:
    index, snippets = store()
    query_embedding = model.encode([question], convert_to_numpy=True)
    _, indices = index.search(query_embedding, top_k)
    results = [snippets[i] for i in indices[0] if i < len(snippets)]
    return " ".join(results)