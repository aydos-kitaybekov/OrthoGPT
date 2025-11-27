import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_variable(var_name: str, default: str = None, required: bool = False) -> str:
    value = os.getenv(var_name, default)
    if required and not value:
        raise ValueError(f"Environment variable '{var_name}' is required but not set.")
    return value

# Configuration
GOOGLE_API_KEY = get_env_variable("GOOGLE_API_KEY", required=True)
NEO4J_URI = get_env_variable("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USERNAME = get_env_variable("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = get_env_variable("NEO4J_PASSWORD", required=True)

DATA_RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")
DATA_PROCESSED_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "processed")
