from src.chains.rag_chain import RAGChain


class QueryService:

    def __init__(self):

        self.chain = RAGChain().build()

    def ask(
        self,
        question: str,
    ) -> str:

        return self.chain.invoke(question)