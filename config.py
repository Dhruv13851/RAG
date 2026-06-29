from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """
    Global application configuration.

    Reads values from .env
    """

    PROJECT_ROOT = Path(__file__).parent

    RAW_DATA_DIR = Path(
        os.getenv("RAW_DATA_DIR", "data/raw")
    )

    EXTRACTED_DATA_DIR = Path(
        os.getenv("EXTRACTED_DATA_DIR", "data/extracted")
    )

    VECTOR_DB_DIR = Path(
        os.getenv("VECTOR_DB_DIR", "data/vector_db")
    )
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")
    
    CHUNK_SIZE = 1000

    CHUNK_OVERLAP = 200

    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )
    EMBEDDING_MODEL = "intfloat/e5-large-v2"

    LLM_MODEL = "llama-3.3-70b-versatile"