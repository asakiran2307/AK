from pathlib import Path
from datetime import datetime

def take_screenshot() -> str:
    try:
        from PIL import ImageGrab
    except ImportError:
        return "Screenshot support requires Pillow. Install it with: pip install pillow"
    folder = Path("data") / "screenshots"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"ak_{datetime.now():%Y%m%d_%H%M%S}.png"
    ImageGrab.grab().save(path)
    return f"Screenshot saved to {path}"
