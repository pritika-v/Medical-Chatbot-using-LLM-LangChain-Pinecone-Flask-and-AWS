from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import Ollama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

load_dotenv()


app=Flask(__name__)

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

embedding = download_embeddings()

index_name="medical-chatbot"
#Embed each chunk and upsert the embeddings into your pinecone index
docsearch=PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3}) #it will retrieve 3 topmost similar answers

chatModel = Ollama(
    model="mistral",   # or llama3 / phi3
    temperature=0
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel,prompt) #understand this. the chatmodel is gpt-4o that we passed
rag_chain = create_retrieval_chain(retriever,question_answer_chain) # we are passing the retriever that we already created

@app.route("/")
def index():
    return render_template('chat.html')

#what function should be done when we have the sen button after the question
@app.route("/get",methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input) #whatever message we are typing, it is given as input
    response=rag_chain.invoke({"input":msg})
    print("Response:",response["answer"]) #gives the output
    return str(response["answer"])


#to execute the app
if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)




