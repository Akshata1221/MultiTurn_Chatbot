# 🤖 Multi-Turn LLM Chatbot

A modern, local-first multi-turn conversational AI web application built using **Streamlit**, **LangChain**, **Ollama (`llama3`)**, and **SQLite**.

---

## 🌟 Key Features

- **💬 Multi-Turn Context**: Remembers previous chat history during active sessions for contextual responses.
- **📂 Multi-Session Support**: Create, switch between, and delete multiple chat sessions from the sidebar.
- **⚡ Streaming Responses**: Tokens stream in real-time for a fluid, ChatGPT-like experience.
- **🔒 Local & Private**: Powered locally via [Ollama](https://ollama.com/) — your data never leaves your machine.
- **💾 Persistent Storage**: All sessions and messages are stored in SQLite and survive page refreshes.
- **🎨 Dark Theme**: Polished dark UI with a custom purple accent color.
- **🛡️ Error Handling**: Graceful messages if Ollama is offline or encounters errors.

---

## 📁 Project Structure

| File | Description |
| :--- | :--- |
| **`app.py`** | Main Streamlit interface — sidebar, sessions, streaming chat, and UI logic. |
| **`chatbot.py`** | LangChain wrapper with error handling and streaming support via Ollama. |
| **`database.py`** | Reusable database module with session & message CRUD helpers. Auto-initializes on import. |
| **`.streamlit/config.toml`** | Streamlit dark theme configuration. |
| **`requirements.txt`** | Python dependencies (`streamlit`, `langchain-ollama`). |

---

## ⚙️ Prerequisites

Before running the application, ensure you have installed:

1. **Python 3.10+**: [Download Python](https://www.python.org/downloads/)
2. **Ollama**: [Download Ollama](https://ollama.com/)

---

## 🚀 Quick Start Guide

### 1. Start Ollama and Pull Model
Make sure Ollama is running, then pull the `llama3` model:
```bash
ollama pull llama3
```

### 2. Set Up Virtual Environment
Create and activate a virtual environment:
```powershell
# Create environment
python -m venv chatbot_env

# Activate on Windows (PowerShell)
.\chatbot_env\Scripts\Activate.ps1
```

### 3. Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Launch the Streamlit web application:
```bash
streamlit run app.py
```

> **Note:** The database (`chats.db`) is created automatically when the app starts — no separate setup step needed.

Open your browser at **[http://localhost:8501](http://localhost:8501)** to start chatting!

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Framework**: [LangChain](https://www.langchain.com/) / `langchain-ollama`
- **Local Model**: [Ollama](https://ollama.com/) (`llama3`)
- **Database**: SQLite3

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
