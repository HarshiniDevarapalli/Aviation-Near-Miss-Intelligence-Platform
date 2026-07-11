import chromadb
from typing import List


class VectorStore:
    """
    Handles storage and retrieval using ChromaDB.
    """

    def __init__(
        self,
        db_path="chroma_db",
        collection_name="aviation_incidents"
    ):

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        ids: List[str],
        documents: List[str],
        embeddings: List[List[float]],
        metadatas: List[dict]
    ):
        """
        Store documents, embeddings and metadata.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query_embedding, k=5):
        """
        Search for the top-k most similar incidents.
        """

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k
        )

        formatted_results = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]
        ids = results["ids"][0]

        for i in range(len(documents)):
            formatted_results.append({
                "id": ids[i],
                "document": documents[i],
                "metadata": metadatas[i],
                "distance": distances[i]
            })

        return formatted_results

    def count(self):
        """Return number of stored documents."""
        return self.collection.count()

    def reset(self):
        """Delete and recreate the collection."""

        self.client.delete_collection(
            self.collection.name
        )

        self.collection = self.client.create_collection(
            self.collection.name
        )