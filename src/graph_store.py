import networkx as nx
import pickle


class GraphStore:
    """
    Stores the aviation knowledge graph and node embeddings.
    """

    def __init__(self):

        self.graph = nx.MultiDiGraph()

        self.node_embeddings = {}

    def add_node(
        self,
        node,
        category
    ):

        self.graph.add_node(
            node,
            category=category
        )

    def add_edge(
        self,
        source,
        target,
        relation
    ):

        self.graph.add_edge(
            source,
            target,
            relation=relation
        )

    def add_embedding(
        self,
        node,
        embedding
    ):

        self.node_embeddings[node] = embedding

    def get_embedding(
        self,
        node
    ):

        return self.node_embeddings[node]

    def get_graph(self):

        return self.graph

    def save(
        self,
        graph_path="graph_data/aviation_graph.gpickle",
        embedding_path="graph_data/node_embeddings.pkl"
    ):

        with open(graph_path, "wb") as f:
            pickle.dump(self.graph, f)

        with open(embedding_path, "wb") as f:
            pickle.dump(self.node_embeddings, f)


    def load(
        self,
        graph_path="graph_data/aviation_graph.gpickle",
        embedding_path="graph_data/node_embeddings.pkl"
        ):

        with open(graph_path, "rb") as f:
            self.graph = pickle.load(f)

        with open(embedding_path, "rb") as f:
            self.node_embeddings = pickle.load(f)