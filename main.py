from fastapi import FastAPI

app = FastAPI(title="Enterprise Support AI")

@app.get("/")
def home():
    return {"message": "Support AI system running"}

@app.get("/health")
def health():
    return {"status": "ok"}
