from __future__ import annotations

from pathlib import Path
from typing import Iterator

import fitz

from src.utils.logger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class PDFSplitter:
    """
    Splits a PDF into temporary chunks.
    """

    def __init__(
        self,
        pages_per_chunk: int = 10,
        temp_dir: str | Path = "temp_chunks",
    ) -> None:

        self.pages_per_chunk = pages_per_chunk
        self.temp_dir = Path(temp_dir)

        self.temp_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def split(
        self,
        pdf_path: str | Path,
    ) -> Iterator[tuple[Path, int, int]]:

        pdf_path = Path(pdf_path)

        document = fitz.open(pdf_path)

        try:

            total_pages = len(document)

            logger.info(
                f"PDF contains {total_pages} pages."
            )

            for start in range(
                0,
                total_pages,
                self.pages_per_chunk,
            ):

                end = min(
                    start + self.pages_per_chunk,
                    total_pages,
                )

                output = (
                    self.temp_dir
                    / f"chunk_{start + 1}_{end}.pdf"
                )

                new_pdf = fitz.open()

                new_pdf.insert_pdf(
                    document,
                    from_page=start,
                    to_page=end - 1,
                )

                new_pdf.save(output)
                new_pdf.close()

                logger.info(
                    f"Created {output.name}"
                )

                yield (
                    output,
                    start + 1,
                    end,
                )

        finally:

            document.close()

    def cleanup(
        self,
        chunk: Path,
    ) -> None:

        try:

            if chunk.exists():
                chunk.unlink()

        except Exception as e:

            logger.warning(
                f"Unable to delete {chunk}: {e}"
            )