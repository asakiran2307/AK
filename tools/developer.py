from pathlib import Path
CODE_EXTENSIONS={".py",".js",".ts",".tsx",".jsx",".java",".c",".cpp",".h",".hpp",".cs",".go",".rs",".sol",".html",".css",".sql",".sh",".ps1"}

def inspect_project(path="."):
    root=Path(path).expanduser().resolve()
    if not root.exists(): return f"Project path not found: {root}"
    files=[p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in CODE_EXTENSIONS][:200]
    counts={}
    for p in files: counts[p.suffix.lower()]=counts.get(p.suffix.lower(),0)+1
    lines=[f"Project: {root}",f"Source files: {len(files)}","Extensions:"]
    lines += [f"  {k}: {v}" for k,v in sorted(counts.items())]
    lines.append("Files:")
    lines += [f"  {p.relative_to(root)}" for p in files[:80]]
    return "\n".join(lines)

def read_text_file(path,max_chars=30000):
    p=Path(path).expanduser().resolve()
    if not p.is_file(): return f"File not found: {p}"
    if p.suffix.lower() not in CODE_EXTENSIONS and p.suffix.lower() not in {".txt",".md",".json",".yaml",".yml"}:
        return "File type is not enabled for text inspection."
    return p.read_text(encoding="utf-8",errors="replace")[:max_chars]
