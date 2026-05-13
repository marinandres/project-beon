from transformers import pipeline
from rag.retrieval import retrieve
from llm.prompt import build_prompt

generator = pipeline("text2text-generation", model="google/flan-t5-small")

def ask(question: str) -> str:
    context = retrieve(question)
    prompt = build_prompt(context=context, question=question)
    response = generator(prompt, max_new_tokens=200)
    return response[0]["generated_text"]