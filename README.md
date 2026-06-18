# Aviation Near-Miss Intelligence Platform

## Overview

The Aviation Near-Miss Intelligence Platform is an AI-powered safety intelligence system designed to analyze and retrieve historical aviation incident reports from NASA's Aviation Safety Reporting System (ASRS).

The platform leverages semantic search, vector embeddings, and Retrieval-Augmented Generation (RAG) techniques to identify incidents that are similar to a newly reported event, uncover recurring hazard patterns, and provide evidence-based safety insights.

The primary objective is to transform large collections of aviation safety reports into an intelligent knowledge system that supports proactive risk identification and operational safety improvements.

---

## Problem Statement

Thousands of aviation incident and near-miss reports are generated every year by pilots, air traffic controllers, maintenance personnel, and flight crews.

Although these reports contain valuable operational knowledge and lessons learned, they are often stored as isolated records and are difficult to search effectively using traditional keyword-based methods.

As a result:

* Similar incidents are frequently overlooked.
* Historical safety knowledge remains underutilized.
* Recurring hazard patterns are difficult to identify.
* Organizations struggle to learn from previous near-miss events.

This project aims to address these challenges by building an intelligent retrieval system capable of understanding the semantic meaning of aviation incident narratives.

---

## Objectives

* Collect and preprocess aviation incident reports from NASA ASRS.
* Build a searchable repository of historical near-miss reports.
* Generate semantic embeddings for incident narratives.
* Retrieve incidents that are contextually similar to a new report.
* Identify recurring hazards and contributing factors.
* Support evidence-based safety analysis and decision-making.
* Establish a foundation for GraphRAG-based risk intelligence.

---

## Dataset

### NASA Aviation Safety Reporting System (ASRS)

The project uses historical incident reports obtained from NASA's Aviation Safety Reporting System (ASRS).

Dataset Characteristics:

* Approximately 20,000 aviation incident reports
* Real-world safety narratives submitted by:

  * Pilots
  * Air Traffic Controllers
  * Flight Crew Members
  * Maintenance Personnel
* Includes:

  * Incident Narratives
  * Primary Problems
  * Contributing Factors
  * Event Outcomes
  * Incident Synopses

---

## Project Workflow

```text
NASA ASRS Reports
        │
        ▼
Data Collection
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Narrative Extraction
        │
        ▼
Embedding Generation
        │
        ▼
Vector Database
        │
        ▼
Semantic Incident Retrieval
        │
        ▼
RAG-Based Analysis
        │
        ▼
Risk Insights & Recommendations
```

---

## Current Progress

### Completed

* Data collection from NASA ASRS
* Merging multiple ASRS exports
* Dataset cleaning and preprocessing
* Header normalization
* Narrative extraction and consolidation
* Creation of structured incident dataset

### In Progress

* Embedding generation using Sentence Transformers
* Vector database construction using ChromaDB
* Semantic incident retrieval engine

### Planned

* Retrieval-Augmented Generation (RAG)
* GraphRAG integration
* Hazard relationship modeling
* Risk escalation analysis
* Interactive visualization dashboard

---

## Tech Stack

### Data Processing

* Python
* Pandas
* NumPy

### Embedding Models

* Sentence Transformers
* BAAI BGE Small

### Vector Database

* ChromaDB

### Large Language Models

* Gemini API

### Graph Analysis (Planned)

* Neo4j
* GraphRAG

### User Interface (Planned)

* Streamlit

---

## Example Use Case

### Input Incident

```text
Aircraft taxiing in dense fog.
Communication delays reported.
Runway signs difficult to identify.
```

### Expected Output

```text
Retrieved Similar Incidents: 5

Common Hazards:
- Poor Visibility
- Taxiway Confusion
- Communication Delays

Potential Outcomes:
- Runway Incursions
- Delayed Departures

Recommended Mitigations:
- Enhanced Ground Lighting
- Improved Communication Procedures
- Visibility Monitoring Systems
```

---

## Repository Structure

```text
Aviation-Near-Miss-Intelligence-Platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── data_preprocessing.ipynb
│
├── src/
│
├── docs/
│
├── requirements.txt
│
└── README.md
```

---

## Future Scope

Future enhancements include:

* Graph-based hazard relationship discovery
* Risk escalation prediction
* Explainable safety recommendations
* Multi-modal incident analysis
* Extension to other safety-critical industries such as railways, manufacturing, and construction

---


