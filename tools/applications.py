import subprocess
from shutil import which

APPS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "explorer": "explorer.exe",
    "cmd": "cmd.exe",
    "powershell": "powershell.exe",
    "terminal": "wt.exe",
    "code": "code",
    "vscode": "code",
}

def open_application(name: str) -> str:
    key = name.strip().lower()
    command = APPS.get(key) or which(key)
    if not command:
        return f"I couldn't find an application named '{name}'."
    subprocess.Popen([command], shell=False)
    return f"Opened {name}."

def close_process(image_name: str) -> str:
    subprocess.run(["taskkill", "/IM", image_name, "/T"], check=False, capture_output=True, text=True)
    return f"Close request sent for {image_name}."
