 pyrefly: ignore [missing-import]
import streamlit as st
from chatbot import get_response_stream
from database import (
    create_session,
    get_sessions,
    get_messages,
    save_message,
    delete_session,
    update_session_title,
)

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Turn LLM Chatbot",
    page_icon="🤖",
    layout="wide",
)

# ── Session State Initialization ─────────────────────────────
if "current_session" not in st.session_state:
    st.session_state.current_session = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# ── Helper: Load messages for a session ──────────────────────
def load_session(session_id):
    """Switch to a session and load its messages from the database."""
    st.session_state.current_session = session_id
    st.session_state.messages = get_messages(session_id)


def start_new_chat():
    """Create a fresh session and clear messages."""
    session_id = create_session("New Chat")
    st.session_state.current_session = session_id
    st.session_state.messages = []


# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🤖 Chatbot")
    st.caption("Powered by Ollama · llama3")
    st.divider()

    # New Chat button
    if st.button("➕  New Chat", use_container_width=True, type="primary"):
        start_new_chat()
        st.rerun()

    st.divider()
    st.markdown("### 💬 Chat History")

    sessions = get_sessions()

    if not sessions:
        st.caption("No previous chats yet.")
    else:
        for session in sessions:
            col1, col2 = st.columns([4, 1])
            with col1:
                label = (
                    f"▶ {session['title']}"
                    if session["id"] == st.session_state.current_session
                    else session["title"]
                )
                if st.button(
                    label,
                    key=f"session_{session['id']}",
                    use_container_width=True,
                ):
                    load_session(session["id"])
                    st.rerun()
            with col2:
                if st.button("🗑️", key=f"del_{session['id']}"):
                    delete_session(session["id"])
                    if st.session_state.current_session == session["id"]:
                        st.session_state.current_session = None
                        st.session_state.messages = []
                    st.rerun()

# ── Main Chat Area ───────────────────────────────────────────
st.title("🤖 Multi-Turn LLM Chatbot")

if st.session_state.current_session is None:
    st.markdown(
        """
        <div style="text-align: center; padding: 80px 20px; opacity: 0.7;">
            <h2>👋 Welcome!</h2>
            <p style="font-size: 1.1rem;">
                Click <b>➕ New Chat</b> in the sidebar to start a conversation,<br>
                or select a previous chat from the history.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    # Display existing messages
    for user_msg, bot_msg in st.session_state.messages:
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            st.write(bot_msg)

    # Chat input
    user_input = st.chat_input("Ask me anything...")

    if user_input:
        # Show user message immediately
        with st.chat_message("user"):
            st.write(user_input)

        # Build conversation history for context
        history = ""
        for prev_user, prev_bot in st.session_state.messages:
            history += f"User: {prev_user}\nAssistant: {prev_bot}\n"

        prompt = (
            "You are a helpful AI assistant.\n\n"
            "Conversation History:\n\n"
            f"{history}\n\n"
            f"User:\n{user_input}\n\n"
            "Assistant:\n"
        )

        # Stream the response token-by-token
        with st.chat_message("assistant"):
            response = st.write_stream(get_response_stream(prompt))

        # Save to session state and database
        st.session_state.messages.append((user_input, response))
        save_message(st.session_state.current_session, user_input, response)

        # Auto-title the session based on the first user message
        if len(st.session_state.messages) == 1:
            title = user_input[:40] + ("..." if len(user_input) > 40 else "")
            update_session_title(st.session_state.current_session, title)
            st.rerun()
