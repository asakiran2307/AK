from brain.ollama_client import OllamaClient

class ModelManager:
    def __init__(self):
        self.client=OllamaClient()
    def status(self):
        ok,data=self.client.health()
        return {"ollama":ok,"model":self.client.model,"detail":data[:500]}
