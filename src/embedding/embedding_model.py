from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.embeddings import Embeddings
from config import Config


class EmbeddingModel:
    """
    Responsible for creating and providing
    the embedding model used throughout the application.
    """

    def __init__(self, model_name: str = Config.EMBEDDING_MODEL):
            self.model_name = model_name
    # Initialize your embedding model here

            self._model = HuggingFaceEmbeddings(
            model_name=model_name
        )

    @property
    def model(self) -> Embeddings:
        return self._model