# Aviation-Near-Miss-Intelligence-Platform

This is an AI-powered aviation safety intelligence system that analyzes historical incident reports from NASA's Aviation Safety Reporting System (ASRS).

The platform uses semantic retrieval and Retrieval-Augmented Generation (RAG) to identify similar incidents, uncover recurring hazards, and provide evidence-based safety insights.

Dataset

NASA ASRS Incident Reports

Current dataset size:

~20,000 aviation incident reports
Merged from multiple ASRS exports
Cleaned and standardized for retrieval tasks

Current Progress
Completed
    Data collection from NASA ASRS
    Dataset merging
    Header normalization
    Narrative extraction
    Incident dataset cleaning
Upcoming
    Text embeddings
    ChromaDB vector store
    Semantic incident retrieval
    RAG pipeline
    GraphRAG risk analysis
    
Tech Stack
Python
Pandas
Sentence Transformers
ChromaDB
Gemini API
Neo4j
Streamlit
