import webbrowser
from urllib.parse import quote_plus

def open_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    webbrowser.open(url)
    return f"Opened {url}"

def search_web(query: str) -> str:
    webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))
    return f"Searching the web for {query}."
