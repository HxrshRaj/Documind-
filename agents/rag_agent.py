from utils.vector_store import (
    build_vector_store
)


def retrieve_knowledge(
    query,
    api_key
):

    vector_store = build_vector_store(
        api_key
    )

    docs = vector_store.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    return context