import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.graph_retriever import GraphRetriever


def main():

    print("Loading Graph Retriever...")

    retriever = GraphRetriever()

    query = "Aircraft taxiing in dense fog"

    print(f"\nQuery: {query}")

    results = retriever.search(
        query,
        top_k=5
    )

    print("\nGraph Retrieval Results")
    print("=" * 80)

    if not results:
        print("No graph results found.")
        return

    for i, item in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 80)

        print(f"Node: {item['node']}")
        print(f"Similarity Score: {item['score']:.4f}")

        print("\nConnected Entities:")

        if item["neighbors"]:
            for neighbor in item["neighbors"]:
                print(f"  • {neighbor}")
        else:
            print("  None")


if __name__ == "__main__":
    main()