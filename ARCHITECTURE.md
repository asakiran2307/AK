# AK Architecture

AK separates reasoning from execution.

Flow: User → Input → Router → Tool Registry → Permission → Executor → Result.

Reasoning-heavy requests use Qwen3 4B for response generation. Qwen never receives unrestricted operating-system execution privileges.

Core components: brain/ for Ollama and Qwen, core/ for routing and execution, tools/ for desktop actions, memory/ for SQLite history, voice/ for optional speech, security/ for authorized lab boundaries, and ui/ for the Tkinter dashboard.