try:
    import tkinter as tk
except Exception:
    tk = None

def read_clipboard() -> str:
    if tk is None:
        return "Clipboard support is unavailable."
    root = tk.Tk(); root.withdraw()
    try:
        return root.clipboard_get()
    except Exception:
        return "Clipboard is empty or unavailable."
    finally:
        root.destroy()

def write_clipboard(text: str) -> str:
    if tk is None:
        return "Clipboard support is unavailable."
    root = tk.Tk(); root.withdraw()
    try:
        root.clipboard_clear(); root.clipboard_append(text); root.update()
        return "Clipboard updated."
    finally:
        root.destroy()
