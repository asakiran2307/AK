import importlib.util
import os
import shutil
import subprocess
import sys
import requests
from config import MODEL, OLLAMA_URL

def check(label, ok, detail=""):
    print(f"[{'OK' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))

def main():
    print("\nAK SYSTEM DOCTOR\n")
    check("Python", sys.version_info >= (3, 10), sys.version.split()[0])
    ollama = shutil.which("ollama") or os.path.expandvars(r"%LOCALAPPDATA%\Programs\Ollama\ollama.exe")
    check("Ollama executable", os.path.exists(ollama), ollama)
    api_ok = False
    models = ""
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        api_ok = r.ok
        models = r.text
    except Exception as exc:
        models = str(exc)
    check("Ollama API", api_ok, "http://127.0.0.1:11434")
    check("Qwen3 4B", MODEL in models, MODEL)
    for pkg in ("requests", "psutil"):
        check(f"Python package: {pkg}", importlib.util.find_spec(pkg) is not None)
    try:
        import psutil
        check("RAM", psutil.virtual_memory().total >= 6 * 1024**3, f"{psutil.virtual_memory().total/1024**3:.1f} GB")
    except Exception:
        check("RAM", False)
    print("\nIf Ollama is installed but the API/model fails, run: ollama serve")
    print("Then verify with: ollama list\n")

if __name__ == "__main__":
    main()
