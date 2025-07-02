# 📚 Study Buddy – Ask Questions on Your Notes

**Study Buddy** is a smart, AI-powered note assistant that allows you to upload your study materials (PDF/DOCX) and ask questions about them. It uses local LLMs with Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers directly from your notes.

---

## 🚀 Features

- 📄 **File Upload** – Supports PDF and DOCX study notes
- 🔍 **RAG Pipeline** – Combines semantic search with local LLMs
- 🧠 **Embeddings** – Uses `sentence-transformers` (MiniLM) to generate vector embeddings
- 🔎 **Vector Search** – Powered by FAISS for fast similarity search
- 🤖 **Local LLM** – Uses Ollama (e.g. Mistral model) for generating context-based answers
- 🌐 **Frontend** – HTML + JavaScript interface for question submission and file upload

---

## 🛠️ Tech Stack

| Part                 | Technology                                | Purpose                                          |
| -------------------- | ------------------------------------------| ------------------------------------------------ |
| ✅ Backend Framework | **FastAPI**                               | To build the API endpoints                       |
| 📄 File Processing  | **PyPDF2, python-docx**                   | To read text from PDF and DOCX                   |
| 🧠 Embeddings       | **sentence-transformers (MiniLM)**        | To convert text chunks into vectors              |
| 🔍 Vector Search    | **FAISS**                                 | To search similar chunks using vector similarity |
| 💾 Data Storage     | **Pickle**                                | To save/load the index                           |
| 🤖 LLM              | **Ollama (e.g. mistral model)**           | To generate answers based on context             |
| 🌐 Frontend         | **HTML + JavaScript (from `index.html`)** | For uploading files and asking questions         |

---

## 🧑‍💻 How It Works

1. **Upload Study Material** – Upload a PDF or DOCX file through the web interface.
2. **Text Chunking** – The file is split into manageable text chunks.
3. **Vector Embedding** – Each chunk is converted to a vector using sentence-transformers.
4. **Vector Indexing** – Vectors are stored using FAISS for similarity search.
5. **RAG** – When a user asks a question, relevant chunks are retrieved and passed to the local LLM via Ollama to generate a response.

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Ollama (installed and running locally)
- Mistral model pulled in Ollama:  
  ```bash
  ollama pull mistral

**#Setup**
# Clone the repo
git clone https://github.com/Himans30/Study-Buddy-Ask-Questions-on-Your-Notes.git
cd Study-Buddy-Ask-Questions-on-Your-Notes

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn app:app --reload

