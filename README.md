
# 🧠 GenAI Assistant (Flask + LangChain + Ollama)

A smart, local AI-powered assistant that stores and recalls your personal/professional information — perfect for resume building, LinkedIn summaries, and personal tracking.

> 💡 Works fully offline using [Ollama](https://ollama.com) and `llama3`. No API keys or billing required.

---

## 🚀 Features

- 🧾 Stores user details: roles, skills, LinkedIn, PAN, etc.
- 🤖 Understands natural prompts like:
  - "My role is Backend Developer"
  - "What is my job title?"
- 💡 Uses local LLMs (`llama3`) via Ollama
- 🧠 Maintains persistent memory using `memory_store.json`
- 🔁 Tested using **Postman**
- 🧳 Next: Dockerize for deployment

---

## ⚙️ Tech Stack

- Python 3.9+
- Flask
- LangChain
- LangChain Community
- Ollama (`llama3` model)
- Postman (for API testing)
- Virtualenv (clean setup)

---

## 📦 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/your-username/genai-resume-assistant.git
cd genai-resume-assistant
```

### 2. Create and activate virtual environment

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama and pull a model

Go to [https://ollama.com/download](https://ollama.com/download) and install for your OS.

Then in terminal:

```bash
ollama pull llama3  # (~4.7 GB)
ollama run llama3
```

> Leave Ollama running in another terminal window.

---

## ▶️ Run the Flask app

```bash
python app.py
```

---

## 🧪 Test with Postman

### POST /ask
- **URL**: `http://localhost:5000/ask`
- **Headers**: `Content-Type: application/json`
- **Body**:

```json
{
  "question": "I am working as a backend developer."
}
```

### GET /memory
- View stored Q&A memory.

---

## 📁 Project Structure

```
genai_resume_assistant/
├── app.py                  # Flask app
├── langchain_handler.py    # LangChain + Ollama logic
├── utils.py                # JSON file handling
├── memory_store.json       # Local memory
├── requirements.txt
```

---

## 🐳 Coming Soon

- Docker support
- Frontend using HTML/CSS
- Export to PDF (resume/summary)
- Upload resume → extract + chat

---

## 🙌 Credits

- Built by Vineet Singh
- Powered by Ollama + LangChain
- Flask-based REST API
