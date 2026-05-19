import streamlit as st

from utils.loader import load_pdf

from utils.vectorstore import create_vectorstore

from utils.reranker import rerank_documents

from utils.helpers import format_context

from utils.chains import get_gemini_response

from utils.prompts import (
    QA_PROMPT,
    SUMMARY_PROMPT
)

from utils.sections import extract_sections


st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.title("⚙️ Settings")

    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

    st.markdown("---")

    st.markdown("### Features")

    st.markdown("""
    ✅ Multi-PDF Chat  
    ✅ Research Summaries  
    ✅ Methodology Extraction  
    ✅ Semantic Search  
    ✅ Citation Answers  
    ✅ Reranking  
    ✅ Literature Review Notes  
    """)

    st.markdown("---")

    st.markdown(
        "Built using LangChain + Gemini + FAISS"
    )


# =========================
# MAIN UI
# =========================

st.title("📚 AI Research Paper Assistant")

st.markdown("""
Upload research papers and interact with them using AI-powered semantic search and RAG.
""")


uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files and api_key:

    all_docs = []

    with st.spinner("Processing Research Papers..."):

        for pdf in uploaded_files:

            docs = load_pdf(pdf)

            all_docs.extend(docs)

        vectorstore, chunks = create_vectorstore(all_docs)

    st.success("Research Papers Processed Successfully!")


    # =========================
    # SUMMARY
    # =========================

    if st.button("Generate Research Summary"):

        full_text = "\n".join(
            [doc.page_content for doc in all_docs]
        )

        summary_prompt = SUMMARY_PROMPT + full_text[:15000]

        summary = get_gemini_response(
            api_key,
            summary_prompt
        )

        st.subheader("📄 Research Summary")

        st.write(summary)


    # =========================
    # SECTION EXTRACTION
    # =========================

    if st.button("Extract Key Sections"):

        full_text = "\n".join(
            [doc.page_content for doc in all_docs]
        )

        sections = extract_sections(full_text)

        st.subheader("Abstract")
        st.write(sections["abstract"])

        st.subheader("Methodology")
        st.write(sections["methodology"])

        st.subheader("Conclusion")
        st.write(sections["conclusion"])


    # =========================
    # LITERATURE REVIEW NOTES
    # =========================

    if st.button("Generate Literature Review Notes"):

        full_text = "\n".join(
            [doc.page_content for doc in all_docs]
        )

        prompt = f"""
        Generate detailed literature review notes
        from the following papers.

        Include:
        - themes
        - methodologies
        - findings
        - research gaps
        - comparisons

        Papers:
        {full_text[:15000]}
        """

        notes = get_gemini_response(
            api_key,
            prompt
        )

        st.subheader("📚 Literature Review Notes")

        st.write(notes)


    # =========================
    # CHAT
    # =========================

    question = st.chat_input(
        "Ask a research question..."
    )

    if question:

        with st.chat_message("user"):

            st.write(question)

        retrieved_docs = vectorstore.similarity_search(
            question,
            k=10
        )

        reranked_docs = rerank_documents(
            question,
            retrieved_docs
        )

        context = format_context(reranked_docs)

        final_prompt = QA_PROMPT.format(
            context=context,
            question=question
        )

        with st.chat_message("assistant"):

            with st.spinner("Generating Response..."):

                answer = get_gemini_response(
                    api_key,
                    final_prompt
                )

                st.write(answer)

        # citations

        with st.expander("View Retrieved Chunks"):

            for i, doc in enumerate(reranked_docs):

                st.markdown(f"### Citation {i+1}")

                st.write(doc.page_content[:1000])
