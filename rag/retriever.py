from google import genai
from configs.settings import GEMINI_API_KEY
from rag.embedding_store import search

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_rag_answer(query: str) -> str:
    """
    Generate grounded answer using retrieved context.
    """
    context_docs = search(query)
    context = "\n".join(context_docs)

    prompt = f"""
You are an enterprise support assistant.

Answer the user question ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text.strip()
