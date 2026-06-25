import logging

from rich.logging import RichHandler


class LoggerFactory:
    """
    Creates configured logger objects.

    Example
    -------

    logger = LoggerFactory.get_logger(__name__)
    """

    @staticmethod
    def get_logger(name: str) -> logging.Logger:

        logger = logging.getLogger(name)

        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)

        handler = RichHandler(
            rich_tracebacks=True,
            markup=True,
            show_path=False
        )

        formatter = logging.Formatter(
            "%(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.propagate = False

        return logger