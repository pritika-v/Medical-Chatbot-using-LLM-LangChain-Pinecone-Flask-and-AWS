# Medical-Chatbot-using-LLM-LangChain-Pinecone-Flask-and-AWS
<!-- In this medical chatbot architecture, the process begins with PDFs containing medical information, which are converted into text embeddings—numerical representations of meaning—using models like SentenceTransformers. These embeddings are stored in Pinecone, a vector database that enables efficient semantic search. When a user asks a question through the Flask web interface, LangChain retrieves the most relevant information from Pinecone based on the question’s meaning and combines it with the user’s query to create a context-rich prompt. This prompt is then sent to a Large Language Model (LLM) such as GPT or an AWS-based model, which generates an accurate, natural-language response. Finally, Flask delivers this response back to the user, creating a seamless, intelligent conversational experience. -->

# HOW TO RUN???
### STEPS:

```bash
git clone (git hub link)

### STEP 1 - CREATE A CONDA ENVIRONMENT AFTER OPENING THE REPOSITORY

```bash
conda create -n medibot python=3.10 -y 
#This command creates a new Conda environment named "medibot" with Python version 3.10 installed. The -n flag specifies the environment name, and -y automatically confirms the installation without prompting for user input. Creating environments this way ensures project isolation, so dependencies from one project do not interfere with another.

```bash
conda activate medibot
#This command switches your terminal session to the "medibot" environment. All subsequent Python commands and package installations will apply specifically to this environment, leaving others untouched. It helps you work with the exact packages needed for your project without affecting anything else.

###STEP 1- INSTALL THE REQUIREMENTS
pip install -r requirements.txt

