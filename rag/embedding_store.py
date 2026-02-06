from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
index = None
dimension = None


def load_documents(file_path: str):
    """
    Load text documents and build FAISS index.
    """
    global documents, index, dimension

    with open(file_path, "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f.readlines() if line.strip()]

    embeddings = model.encode(documents, convert_to_numpy=True)
    embeddings = np.asarray(embeddings, dtype="float32")

    # Ensure 2D
    if embeddings.ndim == 1:
        embeddings = np.expand_dims(embeddings, axis=0)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)


def search(query: str, k: int = 2):
    """
    Search top-k similar documents from FAISS.
    """
    global index, dimension

    if index is None:
        raise ValueError("FAISS index not initialized. Call load_documents() first.")

    query_embedding = model.encode([query], convert_to_numpy=True)
    query_embedding = np.asarray(query_embedding, dtype="float32")

    # Ensure 2D
    if query_embedding.ndim == 1:
        query_embedding = np.expand_dims(query_embedding, axis=0)

    # 🔑 CRITICAL FIX → dimension match check
    if query_embedding.shape[1] != dimension:
        raise ValueError(
            f"Embedding dimension mismatch: query={query_embedding.shape[1]}, index={dimension}"
        )

    distances, indices = index.search(query_embedding, k)

    return [documents[i] for i in indices[0]]
