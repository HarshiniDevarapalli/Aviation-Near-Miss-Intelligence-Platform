from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np


class EmbeddingModel:
    """
    Singleton wrapper around SentenceTransformer.
    The model is loaded only once and reused throughout the application.
    """

    _model = None

    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):

        if EmbeddingModel._model is None:

            print(f"Loading embedding model: {model_name}")

            EmbeddingModel._model = SentenceTransformer(
                model_name
            )

            print("Embedding model loaded successfully!")

        self.model = EmbeddingModel._model

    def encode_documents(
        self,
        documents: List[str]
    ) -> np.ndarray:

        return self.model.encode(
            documents,
            show_progress_bar=True,
            convert_to_numpy=True
        )

    def encode_query(
        self,
        query: str
    ) -> np.ndarray:

        return self.model.encode(
            query,
            convert_to_numpy=True
        )

    def encode(
        self,
        text: str
    ) -> np.ndarray:
        """
        General-purpose embedding for a single string.
        """

        return self.model.encode(
            text,
            convert_to_numpy=True
        )