import pickle
import os
from llama_index.core import PropertyGraphIndex
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.indices.property_graph import SchemaLLMPathExtractor

from src.utils.config import (
    DATA_PROCESSED_DIR, 
    NEO4J_URI, 
    NEO4J_USERNAME, 
    NEO4J_PASSWORD, 
    GOOGLE_API_KEY
)
from src.graph.ontology import ORTHOPEDIC_ENTITIES, ORTHOPEDIC_RELATIONS

def load_nodes(filename="nodes.pkl"):
    input_path = os.path.join(DATA_PROCESSED_DIR, filename)
    print(f"Loading nodes from {input_path}...")
    with open(input_path, "rb") as f:
        nodes = pickle.load(f)
    print(f"Loaded {len(nodes)} nodes.")
    return nodes

def build_graph():
    nodes = load_nodes()
    
    print("Initializing Graph Store...")
    graph_store = Neo4jPropertyGraphStore(
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD,
        url=NEO4J_URI,
    )

    print("Initializing LLM and Embeddings...")
    # Use Gemini for KG extraction
    llm = Gemini(
        model="models/gemini-1.5-pro", 
        api_key=GOOGLE_API_KEY,
        temperature=0.0
    )
    
    # Use local embeddings (same as ingestion)
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    print("Configuring Entity Extractor...")
    kg_extractor = SchemaLLMPathExtractor(
        llm=llm,
        possible_entities=ORTHOPEDIC_ENTITIES,
        possible_relations=ORTHOPEDIC_RELATIONS,
        kg_validation_schema={
            "relationships": ORTHOPEDIC_RELATIONS,
            "entity_types": ORTHOPEDIC_ENTITIES
        },
        strict=True  # Enforce the schema
    )

    print("Building Property Graph Index (this may take a while)...")
    index = PropertyGraphIndex.from_documents(
        [], # We will insert nodes manually or use from_documents if we had documents. 
            # But we have nodes. PropertyGraphIndex accepts nodes in `nodes` param?
            # Actually from_documents takes documents. 
            # Let's check if we can pass nodes directly to constructor or use insert_nodes.
        embed_model=embed_model,
        kg_extractors=[kg_extractor],
        property_graph_store=graph_store,
        show_progress=True
    )
    
    # PropertyGraphIndex.from_documents is convenient but we already have nodes.
    # We can just use the constructor and insert nodes.
    # Or better, convert our nodes back to documents? No, we want to keep the chunks.
    
    # Let's try inserting nodes directly.
    print(f"Inserting {len(nodes)} nodes into the graph...")
    index.insert_nodes(nodes)
    
    print("Graph construction complete!")
    return index

if __name__ == "__main__":
    build_graph()
