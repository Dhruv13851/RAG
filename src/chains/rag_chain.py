from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from src.llm.llm import LLM
from src.retriever.retriever import RetrieverManager


class RAGChain:

    def __init__(self):

        self.retriever = RetrieverManager().get_retriever()

        self.llm = LLM().model

        self.prompt = ChatPromptTemplate.from_template(
            """
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present, say
"I don't know."

Context:
{context}

Question:
{question}
"""
        )

    @staticmethod
    def format_docs(docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    def build(self):

        return (
            {
                "context": self.retriever | self.format_docs,
                "question": RunnablePassthrough(),
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )