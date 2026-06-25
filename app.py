# from config import Config

# from src.services.ingestion_service import (
#     IngestionService,
# )


# def main():

#     pdf = Config.RAW_DATA_DIR / "data.pdf"

#     service = IngestionService()

    
#     for documents in service.ingest(Config.RAW_DATA_DIR / "data.pdf"):
#             vector_store.add_documents(documents)

#     print()

#     print("=" * 60)

#     print("FIRST CHUNK")

#     print("=" * 60)

#     print(chunks[0].page_content)

#     print()

#     print("Metadata")

#     print(chunks[0].metadata)

#     print()

#     print(f"Total Chunks : {len(chunks)}")


# if __name__ == "__main__":
#     main()

# from config import Config
# from src.services.ingestion_service import IngestionService


# def main():
#     service = IngestionService()

#     count = 0

#     for doc in service.ingest(
#         Config.RAW_DATA_DIR / "data.pdf"
#     ):
#         count += 1

#         print("=" * 60)
#         print(f"Chunk {count}")
#         print(doc.page_content[:300])
#         print(doc.metadata)

#     print(f"\nTotal chunks: {count}")


# if __name__ == "__main__":
#     main()

import json

from config import Config
from src.services.ingestion_service import IngestionService


def main():

    service = IngestionService()

    count = 0

    output_file = "chunks.jsonl"

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:

        for doc in service.ingest(
            Config.RAW_DATA_DIR / "data.pdf"
        ):

            count += 1

            record = {
                "chunk_id": count,
                "content": doc.page_content,
                "metadata": doc.metadata,
            }

            f.write(
                json.dumps(
                    record,
                    ensure_ascii=False,
                )
                + "\n"
            )

    print(f"\nTotal chunks: {count}")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()