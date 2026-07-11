from src.embedding_model import EmbeddingModel
from src.vector_store import VectorStore


class Retriever:
    """
    Retrieves the most semantically similar aviation incidents
    from the vector database.
    """

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def search(self, query: str, k: int = 5):
        """
        Search for the top-k most relevant incidents.

        Args:
            query (str): User query
            k (int): Number of results

        Returns:
            list: Retrieved incidents
        """

        print(f"\nSearching for: {query}")

        # Convert query into embedding
        query_embedding = self.embedding_model.encode_query(query)

        # Search ChromaDB
        results = self.vector_store.search(
            query_embedding=query_embedding,
            k=k
        )

        return results