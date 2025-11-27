# OrthoGPT: Orthopedic Graph-based RAG

## Project Overview
OrthoGPT is a Graph-based Retrieval-Augmented Generation (RAG) system designed to answer complex orthopedic questions by combining unstructured PDF data with a structured Knowledge Graph.

## Roadmap

### Phase 1: Data Preparation & Ingestion
- **Goal:** Convert unstructured PDF data into clean, structured text and distinct chunks.
- **Tools:** Unstructured.io, PyMuPDF.
- **Strategy:** Semantic Chunking by medical concepts.

### Phase 2: Ontology Design
- **Goal:** Define Node Types (Anatomy, Condition, Procedure, etc.) and Edge Types (AFFECTS, TREATED_BY, etc.).

### Phase 3: Knowledge Graph Construction
- **Goal:** Extract entities and relationships and build the graph.
- **Stack:** LlamaIndex, Neo4j.
- **Hybrid Indexing:** Vector Index + Graph Database.

### Phase 4: Retrieval Logic
- **Goal:** Query processing using Vector Search + Graph Traversal.

### Phase 5: Tech Stack
- **LLM:** GPT-4o / Gemini 1.5 Pro
- **Orchestration:** LlamaIndex
- **Graph DB:** Neo4j
- **Embeddings:** OpenAI text-embedding-3

### Phase 6: Validation & Safety
- **Goal:** Citation tracking and hallucination checks (RAGAS/DeepEval).

## Project Structure
- `data/`: Raw and processed data storage.
- `src/`: Source code for ingestion, graph construction, and retrieval.
- `notebooks/`: Jupyter notebooks for experimentation.
- `tests/`: Unit and integration tests.
