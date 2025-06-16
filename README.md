# RAG-based Question Answering System

This is a lightweight Retrieval-Augmented Generation (RAG) system built using open-source tools. It allows users to upload documents (PDF or `.txt`) and then ask questions about the content. The system fetches relevant information from the uploaded files and generates context-aware answers using a local LLM.

---

## Features

- Upload & parse `.txt` and `.pdf` files
- Chunk and embed documents using `intfloat/e5-small-v2` model
- Vector search using ChromaDB (persistent)
- Conversational memory for multi-turn Q&A
- Answer generation using `TinyLlama/TinyLlama-1.1B-Chat`
- Unit tests with `pytest`
- (Optional) Docker support
- Returns sources with answers (metadata like page number)

---

## Tech Stack

| Component         | Tool/Model                         | Notes                        |
|------------------|-------------------------------------|------------------------------|
| API Server        | FastAPI                            | Async-ready                  |
| PDF Parsing       | PyMuPDF (`fitz`)                   | Accurate PDF parsing         |
| Embedding Model   | `intfloat/e5-small-v2`             | Fast and accurate            |
| LLM               | `TinyLlama/TinyLlama-1.1B-Chat`    | Lightweight, open-source     |
| Vector DB         | ChromaDB (PersistentClient)        | In-memory with disk backup   |
| Memory            | Simple in-memory dictionary        | Session-level memory         |
| Testing           | `pytest`                           | Unit-tested core functions   |

---


---

## 🧪 Running Locally

### 1. Clone Repo

```bash
git clone https://github.com/your-username/rag-demo
cd rag-demo
```

### 2. Create Virtual Environment (Linux)

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```


### 3. Install Requirements
```
pip install -r requirements.txt
```

### 4. Start the Server
```
fastapi dev app/main.py
```

---


### API Endpoints

##### POST /upload
```
Upload .pdf or .txt file. It gets parsed, chunked, embedded, and indexed.

Body: multipart/form-data
```

#### POST /query
```
Send a question to the system.

{
  "question": "What is the objective of the project?",
  "history": [
    ["Who assigned the project?", "It was given as part of an interview."]
  ]
}
Returns answer and metadata from the most relevant chunks.
```

#### Run Tests
```
pytest
```
