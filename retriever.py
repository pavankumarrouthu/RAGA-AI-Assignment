import faiss
import numpy as np

class RetrieverAgent:
    def __init__(self):
        self.index = None

    def index_embeddings(self, embeddings):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def retrieve(self, query_embedding, k=5):
        distances, indices = self.index.search(query_embedding, k)
        return indices
