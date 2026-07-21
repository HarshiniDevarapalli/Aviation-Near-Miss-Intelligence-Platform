from src.graph_store import GraphStore
from src.embedding_model import EmbeddingModel


class GraphBuilder:
    """
    Builds the aviation knowledge graph from extracted entities.
    """

    def __init__(self):

        self.store = GraphStore()

        self.embedder = EmbeddingModel()

    def build_node_embeddings(self):

        graph = self.store.get_graph()

        print("Embedding graph nodes...")

        for node in graph.nodes():

            embedding = self.embedder.encode(
                str(node)
            )

            self.store.add_embedding(
                node,
                embedding
            )

    def add_incident(
        self,
        entities
    ):

        primary = entities["primary_problem"]

        self.store.add_node(
            primary,
            "Primary Problem"
        )

        result = entities["result"]

        self.store.add_node(
            result,
            "Result"
        )

        self.store.add_edge(
            primary,
            result,
            "leads_to"
        )

        # Airports

        for airport in entities["airports"]:

            self.store.add_node(
                airport,
                "Airport"
            )

            self.store.add_edge(
                airport,
                primary,
                "associated_with"
            )

        # Aircraft

        for aircraft in entities["aircraft"]:

            self.store.add_node(
                aircraft,
                "Aircraft"
            )

            self.store.add_edge(
                aircraft,
                primary,
                "involved_in"
            )

        # Weather

        for weather in entities["weather"]:

            self.store.add_node(
                weather,
                "Weather"
            )

            self.store.add_edge(
                weather,
                primary,
                "contributes_to"
            )

        # Operations

        for operation in entities["operations"]:

            self.store.add_node(
                operation,
                "Operation"
            )

            self.store.add_edge(
                operation,
                primary,
                "performed_during"
            )

        # Contributing Factors

        factors = entities["contributing_factors"]

        if factors:

            for factor in factors.split(";"):

                factor = factor.strip()

                self.store.add_node(
                    factor,
                    "Contributing Factor"
                )

                self.store.add_edge(
                    factor,
                    primary,
                    "contributes_to"
                )

    def get_graph(self):

        return self.store.get_graph()

    def save(self):

        self.build_node_embeddings()

        self.store.save()