import os
from dotenv import load_dotenv

from src.retriever import Retriever
from src.context_builder import ContextBuilder
from src.prompts import build_prompt
from src.gemini_service import GeminiService


class RAGPipeline:
    """
    End-to-end Retrieval-Augmented Generation (RAG) pipeline.

    Workflow:
        User Query
            ↓
        Retriever
            ↓
        Context Builder
            ↓
        Prompt Builder
            ↓
        Gemini
            ↓
        Final Safety Report
    """

    def __init__(self):
        load_dotenv()

        self.retriever = Retriever()
        self.context_builder = ContextBuilder()

        self.gemini = GeminiService(
            os.getenv("GEMINI_API_KEY")
        )

    def run(self, query: str):
        """
        Execute the complete RAG pipeline.

        Args:
            query (str): User query.

        Returns:
            dict: Pipeline output containing the report and retrieved evidence.
        """

        print("Retrieving relevant incidents...")

        results = self.retriever.search(query)

        print("Building context...")

        context = self.context_builder.build_context(
            query,
            results
        )

        print("Generating report...")

        prompt = build_prompt(
            query,
            context
        )

        report = self.gemini.generate_report(
            prompt
        )

        return {
            "query": query,
            "retrieved_incidents": results,
            "context": context,
            "report": report
        }