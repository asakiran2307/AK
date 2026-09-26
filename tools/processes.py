import psutil

def running_processes(limit=30):
    rows=[]
    for p in psutil.process_iter(["pid","name","memory_percent"]):
        try:
            rows.append((p.info["memory_percent"] or 0,p.info["pid"],p.info["name"] or "unknown"))
        except (psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    rows.sort(reverse=True)
    return "\n".join(f"{pid:>6}  {mem:5.1f}%  {name}" for mem,pid,name in rows[:limit]) or "No processes found."

def process_count():
    return f"Running processes: {len(list(psutil.process_iter()))}"
