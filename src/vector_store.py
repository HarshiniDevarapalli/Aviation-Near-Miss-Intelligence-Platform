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

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        k=5
    ):

        return self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k
        )

    def count(self):

        return self.collection.count()

    def reset(self):

        self.client.delete_collection("aviation_incidents")

        self.collection = self.client.create_collection(
            "aviation_incidents"
        )