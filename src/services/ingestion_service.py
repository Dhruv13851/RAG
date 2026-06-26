from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document

from src.loader.pdf_loader import PDFLoader
from src.processor.chunker import ChunkProcessor
from src.embedding.embedding_model import EmbeddingModel
from src.embedding.vector_store import VectorStoreManager
from src.utils.logger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class IngestionService:
    """
    Complete ingestion pipeline.

        PDF
         │
         ▼
    PDFLoader
         │
         ▼
    Markdown
         │
         ▼
    ChunkProcessor
         │
         ▼
    Documents
         │
         ▼
    Embeddings
         │
         ▼
    Vector Store
         │
         ▼
    Save Index
    """

    def __init__(
        self,
        loader: PDFLoader | None = None,
        processor: ChunkProcessor | None = None,
        embedding_model: EmbeddingModel | None = None,
        vector_store_manager: VectorStoreManager | None = None,
    ) -> None:

        self.loader = loader or PDFLoader()
        self.processor = processor or ChunkProcessor()

        self.embedding_model = embedding_model or EmbeddingModel()

        self.vector_store_manager = (
            vector_store_manager
            or VectorStoreManager(
                embeddings=self.embedding_model.model
            )
        )

    def ingest(
        self,
        pdf_path: str | Path,
    ) -> None:
        """
        Build and persist vector index from PDF.
        """

        pdf_path = Path(pdf_path)

        logger.info("=" * 80)
        logger.info(f"Starting ingestion: {pdf_path.name}")
        logger.info("=" * 80)

        documents: list[Document] = []

        for markdown in self.loader.stream_markdown(pdf_path):

            chunks = self.processor.split(
                markdown=markdown,
                metadata={
                    "source": str(pdf_path),
                },
            )

            documents.extend(chunks)

        logger.info(
            f"Generated {len(documents)} chunks."
        )

        vector_store = self.vector_store_manager.create(
            documents=documents
        )

        self.vector_store_manager.save(
            vector_store
        )

        logger.info(
            "Vector index successfully created and saved."
        )

        logger.info("=" * 80)
        logger.info("Ingestion completed.")
        logger.info("=" * 80)