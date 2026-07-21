from src.data_loader import DataLoader
from src.entity_extractor import EntityExtractor
from src.graph_builder import GraphBuilder


def main():

    print("Loading incidents...")

    loader = DataLoader()

    incidents = loader.load_data()

    print(f"Loaded {len(incidents)} incidents.")

    extractor = EntityExtractor()

    builder = GraphBuilder()

    for incident in incidents:

        entities = extractor.extract(incident)

        builder.add_incident(entities)

    builder.save()

    graph = builder.get_graph()

    print()

    print("==============================")

    print("Knowledge Graph Built!")

    print(f"Nodes : {graph.number_of_nodes()}")

    print(f"Edges : {graph.number_of_edges()}")

    print("==============================")


if __name__ == "__main__":

    main()