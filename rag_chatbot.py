from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
PDF_PATH = "C:/Users/precious/Desktop/computech python/llm_project/rfps/sample_rfp.pdf"

loader = PyPDFLoader(PDF_PATH)
pages = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
documents = text_splitter.split_documents(pages)
print(f"✅ Loaded and split {len(documents)} chunks from PDF")
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents,
    embedding_model,
    persist_directory="chroma_db"
)
vectorstore.persist()
print("✅ ChromaDB persisted successfully")

llm = Ollama(model="mistral")  

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)


query = "What is the scope of work in this RFP?"
result = qa_chain(query)

print("\n=== QUESTION ===")
print(query)

print("\n=== ANSWER ===")
print(result["result"])

print("\n=== SOURCE CHUNKS ===")
for doc in result['source_documents']:
    print("---\n", doc.page_content[:300])  
