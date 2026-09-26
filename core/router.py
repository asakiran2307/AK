from pathlib import Path
from core.registry import Tool, ToolRegistry
from tools.system import system_info
from tools.files import list_files
from tools.applications import open_application
from tools.browser import search_web, open_url
from tools.clipboard import read_clipboard, write_clipboard
from tools.network import network_info
from tools.screenshots import take_screenshot

class Router:
    def __init__(self):
        self.registry=ToolRegistry()
        self._register()

    def _register(self):
        for tool in [
            Tool("system_info","Show CPU, RAM and disk status",system_info),
            Tool("open_application","Open a Windows application",open_application),
            Tool("search_web","Search the web",search_web),
            Tool("open_url","Open a URL",open_url),
            Tool("list_files","List files in a directory",list_files),
            Tool("read_clipboard","Read clipboard text",read_clipboard),
            Tool("write_clipboard","Write clipboard text",write_clipboard,risk="medium",requires_confirmation=True),
            Tool("take_screenshot","Take a desktop screenshot",take_screenshot),
            Tool("network_info","Show local network information",network_info),
        ]: self.registry.register(tool)

    def direct(self,text):
        t=text.strip(); low=t.lower()
        if low in {"system info","system status","show system info","show system status"}: return "system_info",{}
        if low in {"screenshot","take screenshot","take a screenshot"}: return "take_screenshot",{}
        if low in {"network info","show my ip","show ip address"}: return "network_info",{}
        if low in {"list files","show files"}: return "list_files",{"path":Path.home()}
        if low=="read clipboard": return "read_clipboard",{}
        if low.startswith("search web "): return "search_web",{"query":t[11:].strip()}
        if low.startswith("open "):
            target=t[5:].strip()
            return ("open_url",{"url":target}) if target.startswith(("http://","https://")) else ("open_application",{"name":target})
        return None
