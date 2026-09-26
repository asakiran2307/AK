import sqlite3
from config import MEMORY_DB

class ReminderStore:
    def __init__(self):
        self.db=sqlite3.connect(MEMORY_DB)
        self.db.execute("CREATE TABLE IF NOT EXISTS reminders (id INTEGER PRIMARY KEY AUTOINCREMENT,text TEXT NOT NULL,due_at TEXT NOT NULL,done INTEGER DEFAULT 0)")
        self.db.commit()
    def add(self,text,due_at):
        self.db.execute("INSERT INTO reminders(text,due_at) VALUES(?,?)",(text,due_at)); self.db.commit()
        return "Reminder created."
    def list_pending(self):
        rows=self.db.execute("SELECT id,text,due_at FROM reminders WHERE done=0 ORDER BY due_at").fetchall()
        return "\n".join(f"{i}: {t} — {d}" for i,t,d in rows) or "No pending reminders."
    def complete(self,reminder_id):
        self.db.execute("UPDATE reminders SET done=1 WHERE id=?",(reminder_id,)); self.db.commit()
        return "Reminder completed."
