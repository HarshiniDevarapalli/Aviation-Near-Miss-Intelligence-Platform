from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np


class EmbeddingModel:
    """
    Handles text embedding using Sentence Transformers.
    """

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        print("Embedding model loaded successfully!")

    def encode_documents(self, documents: List[str]) -> np.ndarray:
        """
        Generate embeddings for multiple documents.
        """
        return self.model.encode(
            documents,
            show_progress_bar=True,
            convert_to_numpy=True
        )

    def encode_query(self, query: str) -> np.ndarray:
        """
        Generate embedding for a single query.
        """
        return self.model.encode(
            query,
            convert_to_numpy=True
        )