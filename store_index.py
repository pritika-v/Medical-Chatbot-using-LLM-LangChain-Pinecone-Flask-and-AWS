from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY

extracted_data=load_pdf_files(data='data/')
minimal_docs = filter_to_minimal_docs(extracted_data)
texts_chunk=text_split(minimal_docs)

embedding = download_embeddings()

pinecone_api_key=PINECONE_API_KEY
pc=Pinecone(api_key=pinecone_api_key)

index_name="medical-chatbot"

existing_indexes=[index.name for index in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384, #---dimension of the embedding-- more dimension, more information in one vector #the embedding model we are using is sentence transformers and it give 384 dimension vector
        metric="cosine", #Cosine similarity
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index=pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunk,
    embedding=embedding,
    index_name=index_name
)
