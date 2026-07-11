import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.vector_store import VectorStore

store = VectorStore()

print("Documents stored:", store.count())