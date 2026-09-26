from brain.ollama_client import OllamaClient
from brain.prompts import SYSTEM_PROMPT

class Planner:
    def __init__(self, client=None):
        self.client = client or OllamaClient()

    def answer(self, user_text: str, history: list[tuple[str, str]]) -> str:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for role, content in history[-8:]:
            messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": user_text})
        return self.client.chat(messages)
