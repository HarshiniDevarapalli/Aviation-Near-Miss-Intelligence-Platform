import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.retriever import Retriever


def main():

    retriever = Retriever()

    query = "Aircraft taxiing in dense fog"

    results = retriever.search(query)

    print("\nTop Results")
    print("=" * 80)

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 80)

        print(f"ID: {result['id']}")
        print(f"Distance: {result['distance']:.4f}")

        print("\nMetadata")
        print(result["metadata"])

        print("\nDocument")
        print(result["document"][:800])
        print()


if __name__ == "__main__":
    main()