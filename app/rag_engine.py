import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.text_chunks = []

    def build_index(self, chunks):
        embeddings = self.model.encode(chunks)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.text_chunks = chunks

    def save_index(self, path='faiss_index/index.pkl'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump((self.index, self.text_chunks), f)

    def load_index(self, path='faiss_index/index.pkl'):
        with open(path, 'rb') as f:
            self.index, self.text_chunks = pickle.load(f)

    def search(self, query, top_k=3):
        query_vec = self.model.encode([query])
        D, I = self.index.search(query_vec, top_k)
        return [self.text_chunks[i] for i in I[0]]
