# from config import Config
# from src.services.ingestion_service import IngestionService


# def main():

#     service = IngestionService()

#     service.ingest(
#         Config.RAW_DATA_DIR / "data.pdf"
#     )

#     print("\nPDF indexed successfully.")


# if __name__ == "__main__":
#     main()

from config import Config

from src.services.ingestion_service import IngestionService
from src.services.query_service import QueryService


# def ingest():

#     service = IngestionService()

#     service.ingest(
#         Config.RAW_DATA_DIR / "data.pdf"
#     )

#     print("PDF indexed successfully.")


def chat():

    service = QueryService()

    while True:

        question = input("\nYou : ")

        if question.lower() in {
            "exit",
            "quit",
        }:
            break

        answer = service.ask(question)

        print(f"\nBot : {answer}")


def main():

    print("1. Ingest PDF")
    print("2. Chat")

    choice = input("Choice : ")

    if choice == "1":
        exit

    elif choice == "2":
        chat()


if __name__ == "__main__":
    main()