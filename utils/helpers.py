def format_context(docs):

    context = ""

    for i, doc in enumerate(docs):

        context += f"\nChunk {i+1}:\n"

        context += doc.page_content

        context += "\n"

    return context
