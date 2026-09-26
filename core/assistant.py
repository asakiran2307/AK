from brain.planner import Planner
from core.audit import audit
from core.executor import ToolExecutor
from core.permissions import PermissionManager
from core.router import Router
from memory.database import Memory

class Assistant:
    def __init__(self):
        self.memory = Memory()
        self.router = Router()
        self.permissions = PermissionManager()
        self.executor = ToolExecutor(self.router.registry, self.permissions)
        self.planner = Planner()

    def respond(self, text: str) -> str:
        self.memory.add("user", text)
        direct = self.router.direct(text)
        if direct:
            name, args = direct
            tool = self.router.registry.get(name)
            confirmed = False
            if tool and tool.requires_confirmation:
                confirmed = self.permissions.confirm_console(name)
                if not confirmed:
                    return "Action cancelled."
            result = self.executor.execute(name, confirmed=confirmed, **args)
            self.memory.add("assistant", result)
            return result
        try:
            answer = self.planner.answer(text, self.memory.recent(10))
        except Exception as exc:
            audit("ollama failure=%s", exc)
            answer = f"Qwen3 is unavailable right now. Start Ollama and verify qwen3:4b.\n\n{exc}"
        self.memory.add("assistant", answer)
        return answer
