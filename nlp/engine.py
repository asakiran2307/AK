import re
from dataclasses import dataclass

@dataclass
class Intent:
    name: str
    confidence: float
    args: dict

class IntentEngine:
    # Lightweight local NLP: no internet, no model download, no heavy ML dependency.
    PATTERNS = [
        ("system_info", [r"\b(system|pc|computer)\b.*\b(info|information|status|specs|details)\b", r"\b(cpu|ram|memory)\b.*\b(status|usage|info)\b"]),
        ("screenshot", [r"\b(take|capture)\b.*\bscreenshot\b", r"\bscreenshot\b"]),
        ("network_info", [r"\b(network|ip|internet)\b.*\b(info|information|status|address|details)\b", r"\bshow\s+(my\s+)?ip\b"]),
        ("process_count", [r"\bhow many\s+(running\s+)?processes\b", r"\bprocess\s+count\b"]),
        ("running_processes", [r"\b(list|show)\b.*\b(processes|running processes)\b"]),
        ("read_clipboard", [r"\b(read|show|get)\b.*\bclipboard\b"]),
        ("list_files", [r"\b(list|show)\b.*\b(files|folder|directory)\b"]),
        ("search_web", [r"^(search|google|look up)\b(?:\s+the)?\s+(.+)$"]),
        ("open_url", [r"\b(open|go to|visit)\s+(https?://\S+|www\.\S+)$"]),
        ("open_application", [r"^(open|launch|start|run)\s+(.+)$"]),
        ("inspect_project", [r"\b(inspect|analyze|scan)\s+(?:the\s+)?project\s+(.+)$"]),
        ("read_text_file", [r"^(read|open)\s+(?:file\s+)?(.+\.(?:txt|md|py|js|ts|json|csv|log|xml|yaml|yml))$"]),
    ]

    def classify(self, text):
        raw = text.strip()
        low = raw.lower()
        for name, patterns in self.PATTERNS:
            for pattern in patterns:
                m = re.search(pattern, low, re.I)
                if not m:
                    continue
                args = {}
                if name == "search_web":
                    args["query"] = m.group(2).strip()
                elif name == "open_url":
                    args["url"] = m.group(2).strip()
                elif name == "open_application":
                    args["name"] = m.group(2).strip()
                elif name == "inspect_project":
                    args["path"] = m.group(1 if m.lastindex == 1 else 2).strip()
                elif name == "read_text_file":
                    args["path"] = m.group(1 if m.lastindex == 1 else 2).strip()
                elif name == "list_files":
                    args["path"] = "."
                return Intent(name, 0.97, args)
        return Intent("unknown", 0.0, {})

    def help_text(self):
        return (
            "I can currently execute: system info, screenshots, network info, "
            "processes, clipboard reading, file listing, web search, opening apps/URLs, "
            "project inspection, and text-file reading. For other requests I can use Qwen3 "
            "when Ollama is available."
        )
