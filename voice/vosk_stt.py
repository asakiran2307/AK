from pathlib import Path

class VoskSTT:
    def __init__(self,model_path="models/vosk"):
        self.model_path=Path(model_path)
        self.model=None
        self.recognizer=None
    def available(self):
        return self.model_path.exists()
    def load(self):
        if not self.available(): return False,"Vosk model directory not found."
        try:
            from vosk import Model,KaldiRecognizer
            self.model=Model(str(self.model_path))
            self.recognizer=KaldiRecognizer(self.model,16000)
            return True,"Vosk ready."
        except Exception as exc:
            return False,str(exc)
