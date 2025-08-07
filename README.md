RFP Chatbot

This project is an interactive chatbot built with Streamlit, LangChain, and Ollama to help users analyze and query RFP (Request for Proposal) documents.

Initial Key Features

Upload and preview RFP PDF documents

Ask multiple questions without reloading the app

Keep track of question/answer history

Select model: mistral, llama2, or llama3

Generate RFP summary

Export Q&A chat history to Word

Simple and clean interface

Challenges
latency with the frontend user interface is slow.
Azure Blob Storage: Store the chat history in a storage container.
Working with One Document from Blob:
When dealing with multiple documents (RFPs, in this case), Azure AI Foundry may not allow easy filtering or focusing on just one document at a time. 
Ensure that each document from Blob Storage is indexed properly. This way, you can refine your queries using metadata_storage_name or other metadata properties as filters.
Free API Keys: Upon signing up, OpenAI offers $18 worth of free tokens for new users. This should cover you for some initial queries.
Setup Instructions

1. Clone the Repository

git clone https://github.com/PelinaP/rfp-chatbot.git
cd rfp-chatbot

2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Requirements

pip install -r requirements.txt

4. Run the App Locally

streamlit run app.py

Deployment

You can deploy this app to Streamlit Cloud by connecting your GitHub repository and selecting app.py as the entry point.

Future Enhancements

File upload previews

Download RFP summary as PDF

Admin login for secure access

Chatbot analytics

License

This project is under the MIT License.

Made by PelinaP

