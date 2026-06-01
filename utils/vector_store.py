from pathlib import Path

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    FAISS
)

from langchain_openai import (
    OpenAIEmbeddings
)


def build_vector_store(
    api_key
):

    knowledge_folder = Path(
        "knowledge_base"
    )

    documents = []

    for file_path in knowledge_folder.glob(
        "*.txt"
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            documents.append(
                file.read()
            )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.create_documents(
        documents
    )

    embeddings = OpenAIEmbeddings(
        api_key=api_key,
        model="text-embedding-3-small"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store