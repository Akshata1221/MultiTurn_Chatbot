import streamlit as st
import sqlite3
from chatbot import get_response

st.set_page_config(page_title="LLM Chatbot")

st.title("🤖 Multi-Turn LLM Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def save_chat(user, bot):
    conn = sqlite3.connect("chats.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO conversations(user_message, bot_response) VALUES (?, ?)",
        (user, bot)
    )

    conn.commit()
    conn.close()

user_input = st.chat_input("Ask me anything...")

if user_input:

    history = ""

    for user, bot in st.session_state.messages:
        history += f"User: {user}\nAssistant: {bot}\n"

    prompt = f"""
You are a helpful AI assistant.

Conversation History:

{history}

User:
{user_input}

Assistant:
"""

    response = get_response(prompt)

    st.session_state.messages.append((user_input, response))

    save_chat(user_input, response)

for user, bot in st.session_state.messages:

    with st.chat_message("user"):
        st.write(user)

    with st.chat_message("assistant"):
        st.write(bot)