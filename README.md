# Aviation Near-Miss Intelligence Platform

## Overview

The Aviation Near-Miss Intelligence Platform is an AI-powered aviation safety intelligence system designed to analyze and retrieve historical aviation incident reports from NASA's Aviation Safety Reporting System (ASRS).

The platform leverages semantic search, dense vector embeddings, and Retrieval-Augmented Generation (RAG) to identify historical incidents that are contextually similar to a newly reported aviation event. By grounding AI-generated safety assessments in real-world historical evidence, the system helps uncover recurring hazard patterns, identify operational risks, and support evidence-based safety analysis.

The primary objective is to transform large collections of aviation safety reports into an intelligent knowledge platform that assists aviation safety analysts, airline operators, and airport authorities in proactive risk identification and operational decision-making.

---

# Problem Statement

Thousands of aviation incident and near-miss reports are generated every year by pilots, air traffic controllers, maintenance personnel, and flight crews.

Although these reports contain valuable operational knowledge and lessons learned, they are typically stored as isolated records, making them difficult to search using conventional keyword-based techniques.

As a result:

- Similar incidents are frequently overlooked.
- Historical operational knowledge remains underutilized.
- Recurring hazard patterns are difficult to identify.
- Organizations struggle to learn effectively from previous near-miss events.

This project addresses these challenges by building an intelligent semantic retrieval system capable of understanding the contextual meaning of aviation incident narratives rather than relying solely on keyword matching.

---

# Objectives

- Collect and preprocess aviation incident reports from NASA's Aviation Safety Reporting System (ASRS).
- Build a semantic repository of historical aviation incidents using ChromaDB.
- Generate dense embeddings for aviation incident narratives using Sentence Transformers.
- Retrieve contextually similar incidents through semantic search.
- Generate AI-assisted Safety Intelligence Reports using Retrieval-Augmented Generation (RAG).
- Identify recurring operational hazards, contributing factors, and historical safety trends.
- Support evidence-based aviation safety analysis and operational decision-making.
- Provide a modular architecture that can be extended with GraphRAG-based aviation risk intelligence in future work.

---

# Key Features

- Semantic search over 16,500+ aviation incident reports
- Retrieval-Augmented Generation (RAG) pipeline
- AI-generated Safety Intelligence Reports
- Historical incident retrieval with similarity scores
- Interactive analytics dashboard
- Operational risk assessment
- Report export functionality
- Enterprise-style Streamlit dashboard

---

# System Architecture

The system follows a Retrieval-Augmented Generation workflow:

```
User Query
      │
      ▼
Embedding Model
(BAAI/bge-small-en-v1.5)
      │
      ▼
Semantic Search
(ChromaDB)
      │
      ▼
Top-K Relevant Incidents
      │
      ▼
Context Builder
      │
      ▼
Prompt Builder
      │
      ▼
Gemini
      │
      ▼
Safety Intelligence Report
```

---

# Project Structure

```text
Aviation-Near-Miss-Intelligence-Platform
│
├── app.py
│   Entry point of the Streamlit application.
│
├── requirements.txt
│   Project dependencies.
│
├── README.md
│   Project overview and setup instructions.
│
├── .env
│   Stores environment variables such as the Gemini API key.
│
├── .gitignore
│   Specifies files and folders ignored by Git.
│
├── .streamlit/
│   └── config.toml
│       Streamlit application configuration and theme settings.
│
├── chroma_db/
│   Persistent ChromaDB vector database storing embeddings.
│
├── data/
│   ├── raw/
│   │   Original NASA ASRS dataset.
│   │
│   └── processed/
│       Cleaned and preprocessed aviation incident reports.
│
├── docs/
│   Project documentation, architecture diagrams, screenshots,
│   and other supporting assets.
│
├── scripts/
│   └── ingest_data.py
│       Generates embeddings for all incident reports and stores
│       them in ChromaDB.
│
├── src/
│   │
│   ├── config.py
│   │   Loads project configuration and environment variables.
│   │
│   ├── data_loader.py
│   │   Loads and preprocesses the ASRS dataset.
│   │
│   ├── embedding_model.py
│   │   Generates dense vector embeddings using the
│   │   BAAI/bge-small-en-v1.5 Sentence Transformer.
│   │
│   ├── vector_store.py
│   │   Handles storage and retrieval operations with ChromaDB.
│   │
│   ├── retriever.py
│   │   Performs semantic similarity search over historical
│   │   aviation incidents.
│   │
│   ├── context_builder.py
│   │   Formats retrieved incidents into structured context for
│   │   the language model.
│   │
│   ├── prompts.py
│   │   Defines prompt templates for AI-generated safety reports.
│   │
│   ├── gemini_service.py
│   │   Interfaces with Google's Gemini model for report generation.
│   │
│   ├── rag_pipeline.py
│   │   Implements the complete Retrieval-Augmented Generation
│   │   workflow from user query to report generation.
│   │
│   └── utils.py
│       Common utility functions used across the backend.
│
├── ui/
│   │
│   ├── __init__.py
│   │   Initializes the UI package.
│   │
│   ├── auth.py
│   │   Handles application authentication and session management.
│   │
│   ├── layout.py
│   │   Defines the overall application layout and page structure.
│   │
│   ├── styles.py
│   │   Custom styling and CSS for the Streamlit interface.
│   │
│   ├── constants.py
│   │   Stores UI constants, labels, and configuration values.
│   │
│   ├── components.py
│   │   Reusable UI components such as cards, sections, and tabs.
│   │
│   ├── analysis.py
│   │   Executes the RAG pipeline and coordinates report generation.
│   │
│   ├── analytics.py
│   │   Generates analytics visualizations and operational insights.
│   │
│   ├── parsers.py
│   │   Parses AI-generated reports for structured presentation.
│   │
│   ├── chart_theme.py
│   │   Defines styling and themes for dashboard visualizations.
│   │
│   └── export.py
│       Supports exporting generated reports.
│
└── tests/
    │
    ├── test_retriever.py
    │   Tests semantic retrieval functionality.
    │
    ├── test_context_builder.py
    │   Tests context construction.
    │
    ├── test_gemini.py
    │   Tests Gemini report generation.
    │
    ├── test_pipeline.py
    │   Tests the complete end-to-end RAG pipeline.
    │
    └── list_models.py
        Lists available Gemini models for validation.
```

---

# Technology Stack

## Programming Language

- Python

## Frontend

- Streamlit
- Plotly

## Artificial Intelligence

- Google Gemini
- Sentence Transformers
- BAAI/bge-small-en-v1.5

## Vector Database

- ChromaDB

## Dataset

- NASA Aviation Safety Reporting System (ASRS)

---

# Dataset

This project utilizes publicly available reports from NASA's Aviation Safety Reporting System (ASRS).

The processed dataset contains more than **16,500** aviation incident reports covering domains such as:

- Runway incursions
- Taxiway excursions
- Near mid-air collisions
- Human factors
- Weather-related incidents
- Communication failures
- Aircraft system anomalies

---

# Workflow

1. The user enters an aviation scenario.
2. The query is converted into dense vector embeddings.
3. ChromaDB retrieves the most semantically similar historical incidents.
4. Retrieved incidents are organized into structured context.
5. Gemini generates a Safety Intelligence Report grounded in retrieved evidence.
6. The application presents:
   - Executive Summary
   - Similar Historical Incidents
   - Risk Assessment
   - Recommendations
   - Historical Evidence
   - Analytics Dashboard

---

# Analytics

The platform includes an interactive analytics dashboard that provides:

- Risk distribution
- Primary problem distribution
- Most frequent contributing factors
- Historical incident timeline
- Similarity analysis
- Operational risk insights

---

# Installation

Clone the repository:

```bash
git clone https://github.com/HarshiniDevarapalli/Aviation-Near-Miss-Intelligence-Platform.git

cd Aviation-Near-Miss-Intelligence-Platform
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Running the Application

```bash
streamlit run app.py
```

---

# Running Tests

```bash
python tests/test_retriever.py
python tests/test_context_builder.py
python tests/test_gemini.py
python tests/test_pipeline.py
```

---

# Future Enhancements

Future development of the platform includes:

- GraphRAG integration for relationship-aware aviation risk intelligence.
- Knowledge graph construction from aviation entities (airports, aircraft, weather events, operational hazards, procedures, and contributing factors).
- Multi-hop reasoning across related aviation incidents.
- PDF report generation.
- Real-time aviation safety data ingestion. 
- Trend forecasting and predictive risk analytics.
- Support for multiple Large Language Models (LLMs).

---
## Author

Harshini Devarapalli

devarapalliharshini10@gmail.com
Computer Science and Engineering  
VNR Vignana Jyothi Institute of Engineering & Technology

---

# License

This project is intended for educational and research purposes.
