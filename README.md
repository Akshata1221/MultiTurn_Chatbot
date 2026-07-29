# 🤖 Multi-Turn LLM Chatbot

A modern, local-first multi-turn conversational AI web application built using **Streamlit**, **LangChain**, **Ollama (`llama3`)**, and **SQLite**.

---

## 🌟 Key Features

- **💬 Multi-Turn Context**: Remembers previous chat history during active sessions for contextual responses.
- **🔒 Local & Private**: Powered locally via [Ollama](https://ollama.com/) — your data never leaves your machine.
- **💾 Database Logging**: Automatically persists chat history into an SQLite database (`chats.db`).
- **🎨 Modern UI**: Built with Streamlit's native chat components (`st.chat_message` and `st.chat_input`).

---

## 📁 Project Structure

| File | Description |
| :--- | :--- |
| **`app.py`** | Main Streamlit interface, session state management, and user interaction flow. |
| **`chatbot.py`** | LangChain wrapper connecting to the local Ollama LLM (`llama3`). |
| **`database.py`** | Database creation and schema script for `chats.db`. |
| **`chats.db`** | SQLite database storing conversation records. |
| **`requirements.txt`** | List of Python dependencies (`streamlit`, `langchain-ollama`). |

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

### 4. Initialize Database
Create the `chats.db` database and `conversations` table:
```bash
python database.py
```

### 5. Run the Application
Launch the Streamlit web application:
```bash
streamlit run app.py
```

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
