import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain_chains import RetrievalQA
import os
import shutil


st.set_page_config(page_title="RFP Chatbot")
st.title(" RFP Chatbot")


uploaded_file = st.file_uploader("Upload an RFP PDF", type=["pdf"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp,write(uploaded_file.read())
        temp_path = tmp.name
loader=
query = st.text_input("Ask a question about the RFP document:")

temp_path = "uploaded_rfp.pdf"
db_dir = "chroma_db"

if uploaded_file is not None:
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())
    
   
    if os.path.exists(db_dir):
        try:
            shutil.rmtree(db_dir)
        except Exception as e:
            st.error(f"Error cleaning DB directory: {e}")

 
    loader = PyPDFLoader(temp_path)
    pages = loader.load_and_split()

   
    embedding_model = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    vectorstore = Chroma.from_documents(
        documents=pages,
        embedding=embedding_model,
        persist_directory=db_dir
    )

    st.success("RFP uploaded and indexed successfully.")

    if query:
        retriever = vectorstore.as_retriever()
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs])

       
        llm = Ollama(model="mistral")
        prompt = f"Answer the following question based on the RFP context:\n\n{context}\n\nQuestion: {query}"
        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response)
