import os
import subprocess
import webbrowser
from pathlib import Path
from tools.system import system_info
from tools.files import list_files

class Router:
    def handle(self, text):
        t = text.lower().strip()

        if t in {"system info", "system status", "show system info", "show system status"}:
            return system_info()

        if t.startswith("open "):
            target = text[5:].strip()
            apps = {
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "explorer": "explorer.exe",
                "cmd": "cmd.exe",
                "powershell": "powershell.exe",
            }
            if target.lower() in apps:
                subprocess.Popen(apps[target.lower()])
                return f"Opened {target}."
            webbrowser.open("https://www.google.com/search?q=" + target.replace(" ", "+"))
            return f"I opened a web search for {target}."

        if t.startswith("search web "):
            q = text[11:].strip()
            webbrowser.open("https://www.google.com/search?q=" + q.replace(" ", "+"))
            return f"Searching the web for {q}."

        if t in {"list files", "show files"}:
            return list_files(Path.home())

        return None
