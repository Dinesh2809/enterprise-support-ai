# Enterprise Support AI — Agentic GenAI Ticket Automation

An **enterprise-grade, multi-agent support automation system** built using **FastAPI, Google Gemini, and FAISS-based Retrieval-Augmented Generation (RAG)**.
The system classifies support intent, detects priority, retrieves grounded knowledge, and generates accurate AI responses through a centralized **agentic orchestration pipeline**.

---

## 🚀 Key Features

* **Agentic AI Architecture**
  Multi-stage pipeline with intent detection, priority triage, and RAG-grounded reasoning.

* **Intent Classification Agent**
  Uses Gemini LLM to categorize incoming support tickets.

* **Priority Detection Agent**
  Automatically determines urgency (low, medium, high) for faster resolution.

* **FAISS Vector Search (RAG)**
  Retrieves relevant enterprise knowledge before generating responses to ensure **grounded and factual answers**.

* **Central Orchestrator**
  Coordinates all AI agents into a **single production-ready decision pipeline**.

* **FastAPI Production Backend**
  Exposes structured REST endpoints with interactive **Swagger UI**.

---

## 🧠 System Architecture

```
User Ticket
    ↓
Intent Agent (Gemini)
    ↓
Priority Agent
    ↓
FAISS RAG Retrieval
    ↓
Grounded LLM Response
    ↓
Final Structured JSON API
```

This mirrors **real enterprise copilot architectures** used in modern AI products.

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Uvicorn
* **LLM:** Google Gemini
* **Vector DB:** FAISS
* **Embeddings:** Sentence-Transformers (MiniLM)
* **Config & Security:** Python-dotenv
* **Language:** Python 3.11+

---

## 📂 Project Structure

```
enterprise-support-ai/
│
├── agents/              # Intent & priority agents
├── orchestrator/        # Central agentic pipeline
├── rag/                 # FAISS embedding + retrieval
├── data/                # Knowledge base documents
├── configs/             # Environment settings
├── main.py              # FastAPI entry point
├── requirements.txt
└── render.yaml          # Cloud deployment config
```

---

## ⚙️ Local Setup

### 1️⃣ Clone repository

```bash
git clone https://github.com/Dinesh2809/enterprise-support-ai.git
cd enterprise-support-ai
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add environment variable

Create `.env`:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run server

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---
