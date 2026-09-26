import socket

def network_info() -> str:
    host = socket.gethostname()
    try:
        ip = socket.gethostbyname(host)
    except Exception:
        ip = "Unavailable"
    return f"Hostname: {host}\nLocal IP: {ip}"
