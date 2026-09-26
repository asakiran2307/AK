import sqlite3
from config import MEMORY_DB

class Memory:
    def __init__(self):
        self.db = sqlite3.connect(MEMORY_DB)
        self.db.execute("""CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        self.db.commit()

    def add(self, role, content):
        self.db.execute("INSERT INTO messages(role, content) VALUES(?, ?)", (role, content))
        self.db.commit()

    def recent(self, limit=12):
        rows = self.db.execute(
            "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
        return list(reversed(rows))
