import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.entity_extractor import EntityExtractor
from src.graph_builder import GraphBuilder


incident = {
    "document": """
    An A320 was taxiing at JFK during dense fog.
    The aircraft experienced a runway excursion.
    """,
    "metadata": {
        "primary_problem": "Airport",
        "contributing_factors": "Weather; Human Factors",
        "result": "Flight Crew Regained Aircraft Control"
    }
}

extractor = EntityExtractor()

entities = extractor.extract(incident)

print("\nExtracted Entities")
print("=" * 60)

for key, value in entities.items():
    print(f"{key}: {value}")

builder = GraphBuilder()

builder.add_incident(entities)

graph = builder.get_graph()

print("\nGraph Statistics")
print("=" * 60)

print(f"Nodes : {graph.number_of_nodes()}")
print(f"Edges : {graph.number_of_edges()}")

builder.save()