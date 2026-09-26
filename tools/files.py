from pathlib import Path

def list_files(path=None):
    p = Path(path or Path.cwd()).expanduser().resolve()
    if not p.exists():
        return f"Directory not found: {p}"
    if not p.is_dir():
        return f"Not a directory: {p}"
    items = sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    if not items:
        return f"{p}\n(empty)"
    lines = [f"Directory: {p}"]
    for item in items[:80]:
        marker = "[DIR]" if item.is_dir() else "[FILE]"
        lines.append(f"{marker} {item.name}")
    if len(items) > 80:
        lines.append(f"... and {len(items)-80} more")
    return "\n".join(lines)

def file_exists(path):
    return Path(path).expanduser().exists()
