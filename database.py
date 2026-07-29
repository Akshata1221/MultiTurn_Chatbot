import sqlite3

conn = sqlite3.connect("chats.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_response TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully.")