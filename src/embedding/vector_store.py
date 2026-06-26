from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS

class VectorStoreManager:
    """
    Handles creation, persistence,
    loading and retrieval from FAISS.
    """

    def __init__(
        self,
        embeddings: Embeddings,
        index_path: str = "outputs/faiss_index"
    ):
        self.embeddings = embeddings
        self.index_path = Path(index_path)

    def create(self, documents: List[Document]) -> FAISS:
        """
        Create FAISS vector store from documents.
        """
        return FAISS.from_documents(
            documents=documents,
            embedding=self.embeddings
        )

    def save(self, vector_store: FAISS) -> None:
        """
        Persist FAISS index locally.
        """
        self.index_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        vector_store.save_local(
            str(self.index_path)
        )

    def load(self) -> FAISS:
        """
        Load existing FAISS index.
        """
        return FAISS.load_local(
            str(self.index_path),
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def exists(self) -> bool:
        """
        Check whether FAISS index exists.
        """
        return self.index_path.exists()

    def get_retriever(
        self,
        k: int = 5
    ):
        """
        Return LangChain retriever.
        """
        vector_store = self.load()

        return vector_store.as_retriever(
            search_kwargs={"k": k}
        )