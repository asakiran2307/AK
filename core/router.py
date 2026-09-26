from core.registry import Tool, ToolRegistry
from nlp.engine import IntentEngine
from tools.system import system_info
from tools.files import list_files
from tools.applications import open_application
from tools.browser import search_web, open_url
from tools.clipboard import read_clipboard, write_clipboard
from tools.network import network_info
from tools.screenshots import take_screenshot
from tools.processes import running_processes, process_count
from tools.developer import inspect_project, read_text_file

class Router:
    def __init__(self):
        self.registry = ToolRegistry()
        self.nlp = IntentEngine()
        self._register()

    def _register(self):
        tools = [
            Tool("system_info", "Show CPU RAM and disk status", system_info),
            Tool("open_application", "Open a Windows application", open_application),
            Tool("search_web", "Search the web", search_web),
            Tool("open_url", "Open a URL", open_url),
            Tool("list_files", "List files in a directory", list_files),
            Tool("read_clipboard", "Read clipboard text", read_clipboard),
            Tool("write_clipboard", "Write clipboard text", write_clipboard, risk="medium", requires_confirmation=True),
            Tool("take_screenshot", "Take a desktop screenshot", take_screenshot),
            Tool("network_info", "Show local network information", network_info),
            Tool("running_processes", "List active processes", running_processes),
            Tool("process_count", "Count active processes", process_count),
            Tool("inspect_project", "Inspect a source-code project", inspect_project),
            Tool("read_text_file", "Read an approved text/source file", read_text_file),
        ]
        for tool in tools:
            self.registry.register(tool)

    def direct(self, text):
        intent = self.nlp.classify(text)
        if intent.name == "unknown":
            return None
        return intent.name, intent.args
