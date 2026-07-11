from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Handles loading the embedding model and generating embeddings.
    """

    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        """
        Generate embeddings for a list of texts.
        """
        return self.model.encode(
            texts,
            show_progress_bar=True
        )

    def encode_query(self, query):
        """
        Generate embedding for a single query.
        """
        return self.model.encode([query])[0]