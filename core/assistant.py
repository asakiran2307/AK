from brain.ollama_client import OllamaClient
from brain.prompts import SYSTEM_PROMPT
from core.executor import ToolExecutor
from core.permissions import PermissionManager
from core.router import Router
from memory.database import Memory

class Assistant:
    def __init__(self):
        self.memory=Memory()
        self.router=Router()
        self.executor=ToolExecutor(self.router.registry,PermissionManager())
        self.ai=OllamaClient()

    def respond(self,text):
        self.memory.add("user",text)
        direct=self.router.direct(text)
        if direct:
            name,args=direct; tool=self.router.registry.get(name)
            if tool.requires_confirmation and not self.executor.permissions.confirm_console(name):
                return "Action cancelled."
            result=self.executor.execute(name,confirmed=True,**args)
            self.memory.add("assistant",result); return result
        messages=[{"role":"system","content":SYSTEM_PROMPT}]
        for role,content in self.memory.recent(8): messages.append({"role":role,"content":content})
        try:
            answer=self.ai.chat(messages)
        except Exception as exc:
            answer=f"Qwen3 is unavailable. Start Ollama and verify qwen3:4b.\n\n{exc}"
        self.memory.add("assistant",answer)
        return answer
