import sys
import os

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ingestion.ingest import run_ingestion

if __name__ == "__main__":
    print("Starting OrthoGPT Data Ingestion Phase...")
    run_ingestion()
