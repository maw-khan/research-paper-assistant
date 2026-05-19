from sentence_transformers import CrossEncoder


reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_documents(question, docs):

    pairs = [
        [question, doc.page_content]
        for doc in docs
    ]

    scores = reranker_model.predict(pairs)

    scored_docs = list(zip(scores, docs))

    scored_docs.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for score, doc in scored_docs[:5]]
