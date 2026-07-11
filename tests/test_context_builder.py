import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.retriever import Retriever
from src.context_builder import ContextBuilder

retriever = Retriever()

results = retriever.search(
    "Aircraft taxiing in dense fog"
)

builder = ContextBuilder()

context = builder.build_context(
    query="Aircraft taxiing in dense fog",
    retrieved_results=results
)

print(context)