import os
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from src.utils.config import DATA_RAW_DIR, DATA_PROCESSED_DIR, GOOGLE_API_KEY
import pickle

def load_documents():
    print(f"Loading documents from {DATA_RAW_DIR}...")
    # SimpleDirectoryReader uses various file parsers (including PyMuPDF/Unstructured if available)
    # to read files from the directory.
    reader = SimpleDirectoryReader(input_dir=DATA_RAW_DIR, recursive=True)
    documents = reader.load_data()
    print(f"Loaded {len(documents)} document(s).")
    return documents

def chunk_documents(documents):
    print("Initializing Semantic Chunking...")
    # Semantic Chunking requires an embedding model to determine semantic similarity
    # Using a local HuggingFace embedding model to avoid rate limits during ingestion
    embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )
    
    splitter = SemanticSplitterNodeParser(
        buffer_size=1, 
        breakpoint_percentile_threshold=95, 
        embed_model=embed_model
    )
    
    print("Chunking documents...")
    nodes = splitter.get_nodes_from_documents(documents)
    print(f"Created {len(nodes)} chunks from {len(documents)} documents.")
    return nodes

def save_nodes(nodes, filename="nodes.pkl"):
    output_path = os.path.join(DATA_PROCESSED_DIR, filename)
    print(f"Saving processed nodes to {output_path}...")
    with open(output_path, "wb") as f:
        pickle.dump(nodes, f)
    print("Save complete.")

def run_ingestion():
    # Check if there are files in raw directory
    if not os.listdir(DATA_RAW_DIR) or (len(os.listdir(DATA_RAW_DIR)) == 1 and os.listdir(DATA_RAW_DIR)[0] == '.gitkeep'):
        print(f"No files found in {DATA_RAW_DIR}. Please add PDF files to start ingestion.")
        return

    documents = load_documents()
    if documents:
        nodes = chunk_documents(documents)
        save_nodes(nodes)

if __name__ == "__main__":
    run_ingestion()
