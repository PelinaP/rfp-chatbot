# main.py
import streamlit as st
from agents import search, rag

st.set_page_config(page_title="Computech RFP AI Assistant")
st.title("RFP Assistant - Powered by LLM")

query = st.text_input("Ask a question about any RFP you've uploaded")

if query:
    st.subheader("🔍 Searching saved responses...")
    results = search.search_rfps(query)

    if results:
        for res in results:
            st.markdown(f"**📄 File:** `{res[0]}`")
            st.write(res[1][:1000] + "...\n")
    else:
        st.subheader("🤖 Using AI via ChromaDB...")
        response = rag.query_vector_db(query)
        st.write(response)

uploaded = st.file_uploader("Upload a new RFP document (PDF only)", type=["pdf"])
if uploaded:
    st.info("RFP received. Add PDF parsing + saving logic here.")
    # You’ll later link to utils.pdf_extract.extract_text_and_filter() and rag.add_to_vector_db()
