import requests
from config import OLLAMA_URL, MODEL

class OllamaClient:
    def __init__(self, model=MODEL, base_url=OLLAMA_URL):
        self.model = model
        self.base_url = base_url.rstrip("/")

    def health(self):
        try:
            r = requests.get(f"{self.base_url}/api/tags", timeout=4)
            return r.ok, r.text
        except Exception as e:
            return False, str(e)

    def chat(self, messages, temperature=0.3):
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature},
        }
        r = requests.post(f"{self.base_url}/api/chat", json=payload, timeout=180)
        r.raise_for_status()
        data = r.json()
        return data.get("message", {}).get("content", "").strip()
