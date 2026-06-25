from pathlib import Path

from pydantic import BaseModel


class DocumentStatistics(BaseModel):
    """
    Statistics of extracted markdown.
    """

    characters: int

    words: int

    headings: int

    table_rows: int

    images: int


class ExtractedDocument(BaseModel):
    """
    Represents one extracted PDF.
    """

    source_pdf: Path

    markdown_path: Path

    markdown: str

    statistics: DocumentStatistics