from src.retriever import Retriever
from src.context_builder import ContextBuilder
from src.context_fusion import ContextFusion
from src.graph_retriever import GraphRetriever
from src.gemini_service import GeminiService
from src.prompts import build_prompt
from src.config import GEMINI_API_KEY


class RAGPipeline:
    """
    Hybrid RAG Pipeline combining:
    - Semantic Retrieval (ChromaDB)
    - Graph Retrieval (Knowledge Graph)
    - Gemini Report Generation
    """

    def __init__(self):

        self.retriever = Retriever()

        self.graph_retriever = GraphRetriever()

        self.context_builder = ContextBuilder()

        self.context_fusion = ContextFusion()

        self.gemini = GeminiService(
            GEMINI_API_KEY
        )

    def run(self, query):

        print("Retrieving semantic incidents...")

        semantic_results = self.retriever.search(
            query
        )

        print("Building semantic context...")

        semantic_context = self.context_builder.build_context(
            query,
            semantic_results
        )

        print("Retrieving graph relationships...")

        graph_results = self.graph_retriever.search(
            query
        )

        print("Fusing contexts...")

        context = self.context_fusion.build_context(
            semantic_context,
            graph_results
        )

        print("Building prompt...")

        prompt = build_prompt(
            query,
            context
        )

        print("Generating report...")

        report = self.gemini.generate_report(
            prompt
        )

        return {
            "query": query,
            "retrieved_incidents": semantic_results,
            "graph_results": graph_results,
            "context": context,
            "report": report
        }