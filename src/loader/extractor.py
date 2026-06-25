from __future__ import annotations

import gc
from pathlib import Path

from docling.document_converter import (
    DocumentConverter,
)

from src.utils.logger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class DoclingExtractor:

    def extract(self, pdf_path: Path) -> str:

        converter = None
        result = None

        try:

            converter = DocumentConverter()

            result = converter.convert(
                str(pdf_path)
            )

            return result.document.export_to_markdown()

        finally:

            del result
            del converter
            gc.collect()