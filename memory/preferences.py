import sqlite3
from config import MEMORY_DB

class Preferences:
    def __init__(self):
        self.db=sqlite3.connect(MEMORY_DB)
        self.db.execute("CREATE TABLE IF NOT EXISTS preferences (key TEXT PRIMARY KEY,value TEXT NOT NULL)")
        self.db.commit()
    def set(self,key,value):
        self.db.execute("INSERT INTO preferences(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value",(key,str(value)))
        self.db.commit()
    def get(self,key,default=None):
        row=self.db.execute("SELECT value FROM preferences WHERE key=?",(key,)).fetchone()
        return row[0] if row else default
    def all(self):
        return dict(self.db.execute("SELECT key,value FROM preferences").fetchall())
