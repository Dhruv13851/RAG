from langchain_core.retrievers import BaseRetriever

from src.embedding.embedding_model import EmbeddingModel
from src.embedding.vector_store import VectorStoreManager


class RetrieverManager:
    """
    Loads the persisted FAISS vector store and exposes
    a LangChain Retriever.
    """

    def __init__(
        self,
        embedding_model: EmbeddingModel | None = None,
        vector_store_manager: VectorStoreManager | None = None,
        search_type: str = "similarity",
        k: int = 4,
    ):

        self.embedding_model = embedding_model or EmbeddingModel()

        self.vector_store_manager = (
            vector_store_manager
            or VectorStoreManager(
                embeddings=self.embedding_model.model
            )
        )

        self.search_type = search_type
        self.k = k

    def get_retriever(self) -> BaseRetriever:

        vector_store = self.vector_store_manager.load()

        return vector_store.as_retriever(
            search_type=self.search_type,
            search_kwargs={
                "k": self.k
            },
        )