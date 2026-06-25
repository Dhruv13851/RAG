from langchain_core.documents import Document

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from config import Config

from src.utils.logger import LoggerFactory


logger = LoggerFactory.get_logger(__name__)


class ChunkProcessor:
    """
    Responsible for creating chunks.

    Returns LangChain Documents.
    """

    def __init__(self):

        self.text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=Config.CHUNK_SIZE,
                chunk_overlap=Config.CHUNK_OVERLAP,
                separators=[
                    "\n# ",
                    "\n## ",
                    "\n### ",
                    "\n\n",
                    "\n",
                    " ",
                    "",
                ],
            )
        )

    def split(
        self,
        markdown: str,
        metadata: dict,
    ) -> list[Document]:

        logger.info("Creating chunks...")

        docs = [
            Document(
                page_content=markdown,
                metadata=metadata,
            )
        ]

        chunks = self.text_splitter.split_documents(
            docs
        )

        logger.info(
            f"{len(chunks)} chunks created."
        )

        return chunks