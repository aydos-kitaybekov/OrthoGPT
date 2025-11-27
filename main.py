import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ingestion.ingest import run_ingestion
from src.graph.builder import build_graph

if __name__ == "__main__":
    print("Starting OrthoGPT Pipeline...")
    
    # Phase 1: Ingestion
    print("\n--- Phase 1: Data Ingestion ---")
    run_ingestion()
    
    # Phase 3: Graph Construction
    print("\n--- Phase 3: Knowledge Graph Construction ---")
    try:
        build_graph()
    except Exception as e:
        print(f"Graph construction failed: {e}")
        print("Please ensure Neo4j is running and configured in .env")
