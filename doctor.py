import importlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def check(label, fn):
    try:
        value = fn()
        print(f"[OK]   {label}: {value}")
        return True
    except Exception as e:
        print(f"[FAIL] {label}: {e}")
        return False

def main():
    print("\nAK DOCTOR\n=========")
    ok = True
    for mod in ["core.router", "core.assistant", "tools.system", "tools.files", "nlp.engine"]:
        ok &= check(f"import {mod}", lambda m=mod: importlib.import_module(m).__name__)
    ok &= check("system tool", lambda: __import__("tools.system", fromlist=["system_info"]).system_info().splitlines()[0])
    ok &= check("NLP engine", lambda: __import__("nlp.engine", fromlist=["IntentEngine"]).IntentEngine().classify("show system info").name)
    ollama = shutil.which("ollama")
    print(f"[{'OK' if ollama else 'WARN'}]  Ollama: {ollama or 'not found on PATH'}")
    print(f"[INFO] Python: {sys.executable}")
    print(f"[INFO] Project: {ROOT}")
    if not ok:
        print("\nAK core has errors. Fix the [FAIL] items before starting.")
        raise SystemExit(1)
    print("\nAK core is healthy.")
    print("Start with: python main.py")
    if ollama:
        print("Then check Qwen with: ollama list")

if __name__ == "__main__":
    main()
