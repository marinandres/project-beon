from sentence_transformers import SentenceTransformer
from kb.snippet import snippet

MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

def get_embeddings(texts: list[str]):
    return model.encode(texts, convert_to_numpy=True)

# Pre-embed the knowledge base
kb_embeddings = get_embeddings(snippet)