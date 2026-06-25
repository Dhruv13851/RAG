import re

from src.utils.logger import LoggerFactory


logger = LoggerFactory.get_logger(__name__)


class MarkdownCleaner:
    """
    Cleans extracted markdown.
    """

    def clean(self, markdown: str) -> str:

        markdown = self.remove_multiple_blank_lines(markdown)

        markdown = self.remove_trailing_spaces(markdown)

        markdown = self.normalize_tabs(markdown)

        logger.info("Markdown cleaned.")

        return markdown

    @staticmethod
    def remove_multiple_blank_lines(text: str) -> str:

        return re.sub(r"\n{3,}", "\n\n", text)

    @staticmethod
    def remove_trailing_spaces(text: str) -> str:

        return "\n".join(
            line.rstrip()
            for line in text.splitlines()
        )

    @staticmethod
    def normalize_tabs(text: str) -> str:

        return text.replace("\t", "    ")