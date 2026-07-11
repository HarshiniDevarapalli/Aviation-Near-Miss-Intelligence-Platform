import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.rag_pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    query = "Aircraft taxiing in dense fog"

    result = pipeline.run(query)

    print("\n" + "=" * 100)
    print("AVIATION NEAR-MISS INTELLIGENCE REPORT")
    print("=" * 100)

    print(result["report"])

    print("\n" + "=" * 100)
    print("RETRIEVED INCIDENTS")
    print("=" * 100)

    for i, incident in enumerate(result["retrieved_incidents"], start=1):

        metadata = incident["metadata"]

        print(f"\nIncident {i}")
        print("-" * 60)
        print(f"Incident ID : {incident['id']}")
        print(f"Date        : {metadata.get('date', 'Unknown')}")
        print(f"Problem     : {metadata.get('primary_problem', 'Unknown')}")
        print(f"Similarity  : {incident['distance']:.4f}")

    print("\nDone!")


if __name__ == "__main__":
    main()