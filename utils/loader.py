from langchain_community.document_loaders import PyMuPDFLoader
import tempfile
import os


def load_pdf(uploaded_file):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())

        temp_path = tmp_file.name

    loader = PyMuPDFLoader(temp_path)

    documents = loader.load()

    os.remove(temp_path)

    return documents
