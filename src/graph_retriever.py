import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from src.embedding_model import EmbeddingModel
from src.graph_store import GraphStore


class GraphRetriever:

    def __init__(self):

        self.embedder = EmbeddingModel()

        self.store = GraphStore()

        self.store.load()

        self.graph = self.store.get_graph()

    def search(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.embedder.encode(query)
        scores = []

        for node in self.graph.nodes():

            node_embedding = self.store.get_embedding(
                node
            )

            similarity = cosine_similarity(
                [query_embedding],
                [node_embedding]
            )[0][0]

            scores.append(
                (
                    node,
                    similarity
                )
            )

        scores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        top_nodes = scores[:top_k]

        graph_context = []

        for node, score in top_nodes:

            neighbors = list(
                self.graph.neighbors(node)
            )

            graph_context.append(
                {
                    "node": node,
                    "score": float(score),
                    "neighbors": neighbors
                }
            )

        return graph_context