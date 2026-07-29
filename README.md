# 🤖 Multi-Turn LLM Chatbot

A modern, local-first multi-turn conversational AI web application built using **Streamlit**, **LangChain**, **Ollama (`llama3`)**, and **SQLite**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.59-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-llama3-black?logo=ollama)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Key Features

| Feature | Description |
| :--- | :--- |
| 💬 **Multi-Turn Context** | Remembers full conversation history for contextual, coherent responses. |
| 📂 **Multi-Session Support** | Create, switch between, and delete multiple chat sessions from the sidebar. |
| ⚡ **Streaming Responses** | Tokens stream in real-time with a typing cursor for a ChatGPT-like experience. |
| 🔒 **Local & Private** | Runs entirely on your machine via Ollama — no data leaves your system. |
| 💾 **Persistent Storage** | All sessions and messages are stored in SQLite and survive page refreshes. |
| 🏷️ **Auto Session Titles** | Sessions are automatically named based on the first message you send. |
| 🎨 **Dark Theme** | Polished dark UI with a custom purple accent color. |
| 🛡️ **Error Handling** | Graceful error messages if Ollama is offline or encounters issues. |

---

## 📸 Screenshots

> _Run the app locally to see the full UI with dark theme, sidebar session management, and streaming chat._

---

## 📁 Project Structure

```
Multiturnchatbot/
├── .streamlit/
│   └── config.toml        # Dark theme configuration
├── app.py                 # Main Streamlit UI — sidebar, sessions, streaming chat
├── chatbot.py             # LangChain + Ollama wrapper with streaming & error handling
├── database.py            # SQLite module with session & message CRUD helpers
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## ⚙️ Prerequisites

Before running the application, ensure you have installed:

1. **Python 3.10+** → [Download Python](https://www.python.org/downloads/)
2. **Ollama** → [Download Ollama](https://ollama.com/)

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Akshata1221/MultiTurn_Chatbot.git
cd MultiTurn_Chatbot
```

### 2. Start Ollama and Pull Model
Make sure Ollama is running, then pull the `llama3` model:
```bash
ollama pull llama3
```

### 3. Set Up Virtual Environment
Create and activate a virtual environment:

**Windows (PowerShell):**
```powershell
python -m venv chatbot_env
.\chatbot_env\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv chatbot_env
source chatbot_env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
streamlit run app.py
```

> **Note:** The database (`chats.db`) is created automatically when the app starts — no separate setup step is needed.

Open your browser at **[http://localhost:8501](http://localhost:8501)** to start chatting! 🎉

---

## 🧠 How It Works

1. **User sends a message** → The full conversation history is built into the prompt.
2. **Prompt is sent to Ollama** (`llama3`) via LangChain's `OllamaLLM`.
3. **Response streams token-by-token** → displayed with a typing cursor (`▌`) in real-time.
4. **Message pair is saved** to SQLite under the active session.
5. **Session auto-titles** itself based on the first user message.

```
User Input → Build Prompt (with history) → Ollama llama3 → Stream Response → Save to SQLite
```

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **LLM Framework** | [LangChain](https://www.langchain.com/) / `langchain-ollama` |
| **Local Model** | [Ollama](https://ollama.com/) (`llama3`) |
| **Database** | SQLite3 |
| **Language** | Python 3.10+ |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Akshata Patil** — [GitHub](https://github.com/Akshata1221)
