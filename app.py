import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

from utils.pdf_processing import extract_text_from_pdf
from utils.chunking import chunk_text
from utils.embeddings import create_embeddings, model
from utils.vector_store import create_faiss_index, search_index
from utils.rag_pipeline import generate_answer, generate_summary


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(
    page_title="Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)


st.title("📚 AI Research Paper Assistant")

st.markdown(
    "Upload a research paper and chat with it using AI."
)


uploaded_pdf = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)


if uploaded_pdf:

    with st.spinner("Processing Research Paper..."):

        text = extract_text_from_pdf(uploaded_pdf)

        chunks = chunk_text(text)

        embeddings = create_embeddings(chunks)

        index = create_faiss_index(embeddings)

    st.success("Research Paper Processed Successfully!")

    if st.button("Generate Paper Summary"):

        with st.spinner("Generating Summary..."):

            summary = generate_summary(text[:10000])

            st.subheader("Paper Summary")

            st.write(summary)

    question = st.text_input(
        "Ask a question about the paper"
    )

    if question:

        query_embedding = model.encode([question])

        indices = search_index(
            query_embedding,
            index
        )

        retrieved_chunks = [
            chunks[i]
            for i in indices
        ]

        context = "\n".join(retrieved_chunks)

        with st.spinner("Generating Answer..."):

            answer = generate_answer(
                context,
                question
            )

            st.subheader("Answer")

            st.write(answer)
