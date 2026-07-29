import sqlite3
from datetime import datetime

DB_NAME = "chats.db"


def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id INTEGER NOT NULL,
        user_message TEXT,
        bot_response TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()


def create_session(title="New Chat"):
    """Create a new chat session and return its ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessions(title, created_at) VALUES (?, ?)",
        (title, datetime.now())
    )
    session_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return session_id


def get_sessions():
    """Return all sessions ordered by most recent first."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sessions ORDER BY created_at DESC")
    sessions = cursor.fetchall()
    conn.close()
    return sessions


def update_session_title(session_id, title):
    """Update the title of a session."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE sessions SET title = ? WHERE id = ?", (title, session_id))
    conn.commit()
    conn.close()


def delete_session(session_id):
    """Delete a session and all its messages."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM conversations WHERE session_id = ?", (session_id,))
    cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
    conn.commit()
    conn.close()


def save_message(session_id, user_message, bot_response):
    """Save a user/bot message pair to a session."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conversations(session_id, user_message, bot_response, timestamp) VALUES (?, ?, ?, ?)",
        (session_id, user_message, bot_response, datetime.now())
    )
    conn.commit()
    conn.close()


def get_messages(session_id):
    """Return all messages for a session in chronological order."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_message, bot_response FROM conversations WHERE session_id = ? ORDER BY timestamp ASC",
        (session_id,)
    )
    messages = cursor.fetchall()
    conn.close()
    return [(msg["user_message"], msg["bot_response"]) for msg in messages]


# Auto-initialize the database on import
init_db()