from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "qwen3:4b"

APP_NAME = "AK"
MEMORY_DB = DATA_DIR / "memory.sqlite3"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
