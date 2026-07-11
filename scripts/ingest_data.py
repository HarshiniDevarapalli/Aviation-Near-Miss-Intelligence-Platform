import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.data_loader import DataLoader
from src.embedding_model import EmbeddingModel
from src.vector_store import VectorStore


def main():

    # -----------------------------
    # Configuration
    # -----------------------------
    DATA_PATH = "data/processed/asrs_clean_final.csv"
    BATCH_SIZE = 500

    # -----------------------------
    # Load data
    # -----------------------------
    print("Loading dataset...")

    loader = DataLoader(DATA_PATH)

    df = loader.load_data()

    documents = loader.prepare_documents(df)
    metadata = loader.prepare_metadata(df)

    print(f"Loaded {len(documents)} documents.")

    # -----------------------------
    # Load embedding model
    # -----------------------------
    model = EmbeddingModel()

    # -----------------------------
    # Create / Connect ChromaDB
    # -----------------------------
    store = VectorStore()

    print("Connected to ChromaDB.")

    # Uncomment this ONLY if you want to rebuild
    # store.reset()

    # -----------------------------
    # Generate embeddings and store
    # -----------------------------
    total_docs = len(documents)

    for start in range(0, total_docs, BATCH_SIZE):

        end = min(start + BATCH_SIZE, total_docs)

        batch_docs = documents[start:end]
        batch_meta = metadata[start:end]

        print(f"\nProcessing {start} -> {end}")

        batch_embeddings = model.encode_documents(batch_docs)

        ids = [str(i) for i in range(start, end)]

        store.add_documents(
            ids=ids,
            documents=batch_docs,
            embeddings=batch_embeddings.tolist(),
            metadatas=batch_meta
        )

        print(f"Stored {end}/{total_docs}")

    print("\n==============================")
    print("Ingestion Complete!")
    print(f"Documents in ChromaDB: {store.count()}")
    print("==============================")


if __name__ == "__main__":
    main()