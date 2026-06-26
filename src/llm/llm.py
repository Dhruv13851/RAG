from langchain_groq import ChatGroq

from config import Config


class LLM:
    """
    Wrapper around the application's Large Language Model.
    """

    def __init__(self) -> None:

        self.model = ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model=Config.LLM_MODEL,
            temperature=0,
        )