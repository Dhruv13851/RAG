from __future__ import annotations

from pathlib import Path
from typing import Iterator

from langchain_core.documents import Document

from src.loader.pdf_loader import PDFLoader
from src.processor.chunker import ChunkProcessor
from src.utils.logger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class IngestionService:
    """
    Main ingestion pipeline.

    Pipeline:

        PDF
         │
         ▼
    PDFLoader.stream_markdown()
         │
         ▼
    Markdown
         │
         ▼
    ChunkProcessor
         │
         ▼
    LangChain Documents
         │
         ▼
    yield Documents
    """

    def __init__(
        self,
        loader: PDFLoader | None = None,
        processor: ChunkProcessor | None = None,
    ) -> None:

        self.loader = loader or PDFLoader()
        self.processor = processor or ChunkProcessor()

    def ingest(
        self,
        pdf_path: str | Path,
    ) -> Iterator[Document]:
        """
        Stream LangChain Documents from a PDF.

        Parameters
        ----------
        pdf_path : str | Path
            PDF file location.

        Yields
        ------
        Document
            LangChain Document objects.
        """

        pdf_path = Path(pdf_path)

        logger.info("=" * 80)
        logger.info(f"Starting ingestion : {pdf_path.name}")
        logger.info("=" * 80)

        total_chunks = 0

        for markdown in self.loader.stream_markdown(pdf_path):

            documents = self.processor.split(
            markdown=markdown,
            metadata={
                "source": str(pdf_path),
                },
            )

            total_chunks += len(documents)

            for document in documents:
                yield document

        logger.info("=" * 80)
        logger.info(
            f"Ingestion completed. Total Chunks : {total_chunks}"
        )
        logger.info("=" * 80)