import os
import platform
import shutil
from datetime import datetime

def system_info():
    try:
        import psutil
    except ImportError:
        psutil = None
    lines = [
        f"OS: {platform.system()} {platform.release()} ({platform.machine()})",
        f"Computer: {platform.node()}",
        f"Python: {platform.python_version()}",
        f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    ]
    if psutil:
        vm = psutil.virtual_memory()
        disk = shutil.disk_usage(os.path.expanduser("~"))
        lines += [
            f"CPU: {psutil.cpu_percent(interval=0.2):.1f}%",
            f"RAM: {vm.percent:.1f}% used ({vm.used/1024**3:.1f} GB / {vm.total/1024**3:.1f} GB)",
            f"Disk: {disk.used/1024**3:.1f} GB used / {disk.total/1024**3:.1f} GB",
        ]
    return "\n".join(lines)
