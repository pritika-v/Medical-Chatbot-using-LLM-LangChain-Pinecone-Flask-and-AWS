from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

#Extract text from pdf files
def load_pdf_files(data):
    loader=DirectoryLoader(
        data, #the path where the pdfs are
        glob="*.pdf", #even if there are multiple files in your stuff, just download the pdf files
        loader_cls=PyPDFLoader
    )

    documents=loader.load()
    return documents

def filter_to_minimal_docs(docs: List[Document])-> List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects
    containing pnly 'source' in metadata and the original page_content.
    """
    minimal_docs: List[Document]=[]
    for doc in docs:
        src=doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
    return minimal_docs #this will give only the source and the page content

#Split the documents into smaller chunks---Chunking
def text_split(minimal_docs):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500, #500 tokens= 1 chunk
        chunk_overlap=20,
    )
    texts_chunk=text_splitter.split_documents(minimal_docs)
    return texts_chunk

#Download th Embeddings from HuggingFace
def download_embeddings():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings