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
├── src/
│   ├── context_builder.py
│   ├── data_loader.py
│   ├── embedding_model.py
│   ├── gemini_service.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── vector_store.py
│
├── ui/
├── scripts/
├── tests/
├── data/
├── chroma_db/
├── docs/
└── requirements.txt
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
