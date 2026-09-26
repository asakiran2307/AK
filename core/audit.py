import logging
from logging.handlers import RotatingFileHandler
from config import LOG_DIR

LOGGER = logging.getLogger("ak")
if not LOGGER.handlers:
    LOGGER.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOG_DIR / "ak.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    LOGGER.addHandler(handler)

def audit(message: str, *args) -> None:
    LOGGER.info(message, *args)
