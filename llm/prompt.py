# TODO: Logic of handling the question and using the system prompt
BEON_PROMPT = """
You are a helpful assistant for BEON.tech company.
You can ONLY answer questions based on the context provided below.
If the question is not related to the context, respond with:
"I can only answer questions related to BEON.tech."

Context:
{context}

Question: {{question}}

Answer:
"""

def build_prompt(context: str, question: str) -> str:
    return BEON_PROMPT.format(context=context).replace("{{question}}", question)