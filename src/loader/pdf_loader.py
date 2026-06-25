from __future__ import annotations

from pathlib import Path
from typing import Iterator

from src.loader.extractor import DoclingExtractor
from src.loader.pdf_splitter import PDFSplitter
from src.utils.logger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class PDFLoader:
    """
    Process PDF in chunks to reduce memory usage.
    """

    def __init__(self):

        self.splitter = PDFSplitter(
            pages_per_chunk=10
        )

        self.extractor = DoclingExtractor()

    def stream_markdown(
        self,
        pdf_path: str | Path,
    ) -> Iterator[str]:

        pdf_path = Path(pdf_path)

        logger.info(
            f"Extracting PDF: {pdf_path.name}"
        )

        for (
            chunk,
            start_page,
            end_page,
        ) in self.splitter.split(pdf_path):

            try:

                logger.info(
                    f"Processing {chunk.name}"
                )

                markdown = self.extractor.extract(
                    chunk
                )

                if markdown:

                    markdown = (
                        f"\n\n"
                        f"---\n"
                        f"Pages: {start_page}-{end_page}\n"
                        f"---\n\n"
                        f"{markdown}"
                    )

                    yield markdown

            except Exception as e:

                logger.exception(
                    f"Failed on {chunk.name}: {e}"
                )

            finally:

                self.splitter.cleanup(chunk)

        logger.info(
            "Extraction Finished."
        )