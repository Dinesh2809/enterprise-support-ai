from agents.intent_agent import classify_intent
from agents.priority_agent import detect_priority
from rag.retriever import generate_rag_answer


def process_support_ticket(ticket: str) -> dict:
    """
    Full enterprise AI pipeline:
    Intent → Priority → RAG → Final structured response
    """

    # Step 1 — Intent classification
    intent = classify_intent(ticket)

    # Step 2 — Priority detection
    priority = detect_priority(ticket)

    # Step 3 — Grounded answer via RAG
    answer = generate_rag_answer(ticket)

    # Step 4 — Final structured response
    return {
        "ticket": ticket,
        "intent": intent,
        "priority": priority,
        "answer": answer,
    }
