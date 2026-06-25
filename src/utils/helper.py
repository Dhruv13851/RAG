from pathlib import Path

import re

from src.utils.logger import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class FileHelper:
    """
    Generic file helper functions.
    """

    @staticmethod
    def create_directory(path: Path) -> None:
        """
        Creates directory if not exists.
        """

        path.mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def save_markdown(
        markdown: str,
        output_path: Path
    ) -> None:

        FileHelper.create_directory(
            output_path.parent
        )

        output_path.write_text(
            markdown,
            encoding="utf-8"
        )

        logger.info(
            f"Markdown saved -> {output_path}"
        )

    @staticmethod
    def read_markdown(
        path: Path
    ) -> str:

        return path.read_text(
            encoding="utf-8"
        )

    @staticmethod
    def count_words(
        text: str
    ) -> int:

        return len(text.split())

    @staticmethod
    def count_characters(
        text: str
    ) -> int:

        return len(text)

    @staticmethod
    def count_headings(
        markdown: str
    ) -> int:

        headings = re.findall(
            r"^#+\s.*",
            markdown,
            flags=re.MULTILINE
        )

        return len(headings)

    @staticmethod
    def count_tables(
        markdown: str
    ) -> int:

        rows = [
            row
            for row in markdown.split("\n")
            if "|" in row
        ]

        return len(rows)

    @staticmethod
    def count_images(
        markdown: str
    ) -> int:

        return markdown.count("![")