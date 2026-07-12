# Aviation Near-Miss Intelligence Platform

## Overview

The Aviation Near-Miss Intelligence Platform is an AI-powered aviation safety intelligence system designed to analyze and retrieve historical aviation incident reports from NASA's Aviation Safety Reporting System (ASRS).

The platform leverages semantic search, dense vector embeddings, and Retrieval-Augmented Generation (RAG) to identify historical incidents that are contextually similar to a newly reported aviation event. By grounding AI-generated safety assessments in real-world historical evidence, the system helps uncover recurring hazard patterns, identify operational risks, and support evidence-based safety analysis.

The primary objective is to transform large collections of aviation safety reports into an intelligent knowledge platform that assists aviation safety analysts, airline operators, and airport authorities in proactive risk identification and operational decision-making.

---

# Project Highlights

- Semantic search over **16,500+** NASA ASRS aviation incident reports
- Retrieval-Augmented Generation (RAG) pipeline
- Dense vector embeddings using Sentence Transformers
- Persistent semantic retrieval with ChromaDB
- AI-generated Safety Intelligence Reports using Google Gemini
- Interactive analytics dashboard
- Operational risk assessment based on historical evidence
- Enterprise-style Streamlit interface
- Modular architecture designed for future GraphRAG integration

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

- Semantic search using dense vector embeddings
- ChromaDB-powered vector database
- AI-generated Safety Intelligence Reports
- Historical incident retrieval with similarity scores
- Interactive analytics dashboard
- Risk assessment and operational recommendations
- Report export functionality
- Modular Retrieval-Augmented Generation pipeline

---

# System Architecture

The system follows a Retrieval-Augmented Generation (RAG) workflow.

```text
                     User Query
                          │
                          ▼
               Embedding Generation
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
                  Google Gemini
                          │
                          ▼
           Safety Intelligence Report
                          │
                          ▼
          Streamlit Analytics Dashboard
```

---

# Architecture Components

| Component | Responsibility |
|------------|----------------|
| Data Loader | Loads and preprocesses ASRS incident reports |
| Embedding Model | Generates semantic embeddings using Sentence Transformers |
| Vector Store | Stores embeddings and metadata using ChromaDB |
| Retriever | Retrieves semantically similar aviation incidents |
| Context Builder | Formats retrieved incidents into structured context |
| Prompt Builder | Constructs prompts for Gemini |
| Gemini Service | Generates Safety Intelligence Reports |
| Streamlit UI | Presents reports, evidence, and analytics |

---

# Project Structure

```text
Aviation-Near-Miss-Intelligence-Platform
│
├── app.py
│   Entry point of the Streamlit application.
│
├── README.md
│   Project overview and setup instructions.
│
├── requirements.txt
│   Project dependencies.
│
├── .gitignore
│   Specifies files and folders ignored by Git.
│
├── .streamlit/
│   └── config.toml
│       Streamlit application configuration and theme settings.
│
├── chroma_db/
│   Persistent ChromaDB vector database containing semantic embeddings.
│
├── data/
│   ├── raw/
│   │   Original NASA ASRS dataset.
│   │
│   └── processed/
│       Cleaned and preprocessed aviation incident reports.
│
├── docs/
│   Documentation, architecture diagrams, screenshots,
│   and supplementary project resources.
│
├── scripts/
│   └── ingest_data.py
│       Generates embeddings and stores them in ChromaDB.
│
├── src/
│   ├── config.py
│   ├── context_builder.py
│   ├── data_loader.py
│   ├── embedding_model.py
│   ├── gemini_service.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── utils.py
│   └── vector_store.py
│
├── ui/
│   ├── __init__.py
│   ├── analysis.py
│   ├── analytics.py
│   ├── auth.py
│   ├── chart_theme.py
│   ├── components.py
│   ├── constants.py
│   ├── export.py
│   ├── layout.py
│   ├── parsers.py
│   └── styles.py
│
└── tests/
    ├── list_models.py
    ├── test_context_builder.py
    ├── test_gemini.py
    ├── test_pipeline.py
    └── test_retriever.py
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Data Visualization | Plotly |
| Large Language Model | Google Gemini |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| NLP Framework | Sentence Transformers |
| Vector Database | ChromaDB |
| Dataset | NASA Aviation Safety Reporting System (ASRS) |

---

# Dataset

This project utilizes publicly available reports from NASA's Aviation Safety Reporting System (ASRS).

The processed dataset contains more than **16,500** aviation incident reports covering operational domains such as:

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
2. The query is converted into a dense vector embedding.
3. ChromaDB retrieves the most semantically similar historical incidents.
4. Retrieved incidents are formatted into structured context.
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

The platform includes an interactive analytics dashboard providing insights into retrieved incidents, including:

- Primary problem distribution
- Most frequent contributing factors
- Historical incident timeline
- Similarity score analysis
- Operational risk insights
- Trend visualization

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

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Running the Application

Populate the vector database:

```bash
python scripts/ingest_data.py
```

Launch the application:

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
- Knowledge graph construction using aviation entities and operational relationships.
- Multi-hop reasoning across related historical incidents.
- PDF report generation.
- Real-time aviation safety data ingestion.
- Predictive risk analytics and trend forecasting.
- Support for multiple Large Language Models (LLMs).
- Cloud deployment and enterprise authentication.

---

# Documentation

Additional project resources are available in the `docs/` directory, including:

- System architecture diagrams
- Project documentation
- UI screenshots
- Design documents

---

# References

- NASA Aviation Safety Reporting System (ASRS)
- Google Gemini API
- ChromaDB
- Sentence Transformers
- BAAI/bge-small-en-v1.5
- Streamlit
- Plotly

---

# Author

**Harshini Devarapalli**

Computer Science and Engineering  
VNR Vignana Jyothi Institute of Engineering & Technology

**Email:** devarapalliharshini10@gmail.com

**GitHub:**  
https://github.com/HarshiniDevarapalli

**LinkedIn:**  
https://www.linkedin.com/in/harshini-devarapalli-706b23261/

---

# License

This project is intended for educational and research purposes.
