from fastapi import FastAPI
from rag.retriever import generate_rag_answer
from pydantic import BaseModel
from orchestrator.support_orchestrator import process_support_ticket
import os
from rag.embedding_store import load_documents

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(BASE_DIR, "data", "support_docs.txt")

load_documents(DOC_PATH)


from agents.priority_agent import detect_priority

app = FastAPI(title="Enterprise Support AI")

@app.get("/")
def home():
    return {"message": "Support AI system running"}

@app.get("/health")
def health():
    return {"status": "ok"}

from agents.intent_agent import classify_intent


@app.get("/test-intent")
def test_intent():
    sample_ticket = "I am unable to login to my account after password reset."
    intent = classify_intent(sample_ticket)
    return {"intent": intent}

@app.get("/test-priority")
def test_priority():
    sample_ticket = "Payment is failing for all users in production."
    priority = detect_priority(sample_ticket)
    return {"priority": priority}

@app.get("/test-rag")
def test_rag():
    query = "Why is my payment failing?"
    answer = generate_rag_answer(query)
    return {"answer": answer}

class SupportQuery(BaseModel):
    ticket: str


@app.post("/support/query")
def support_query(data: SupportQuery):
    return process_support_ticket(data.ticket)