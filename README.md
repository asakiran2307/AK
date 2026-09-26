# AK — Local JARVIS AI Assistant

AK is a local-first Windows desktop assistant built around Qwen3 4B + Ollama for a Windows machine with about 8 GB RAM.

## Current foundation
- Local Qwen3 4B chat through Ollama
- Fast direct command routing
- Registered tool architecture
- Permission checks
- Rotating audit log
- Windows application launching
- System information and file listing
- Browser search and URL opening
- Clipboard read/write
- Desktop screenshots
- Local network information
- SQLite conversation memory
- Optional speech adapters
- Authorized security-lab scope object
- Tkinter desktop dashboard
- Doctor, setup and run scripts

## Architecture
User → Router → Tool Registry → Permission Layer → Tool Executor

Reasoning-heavy requests → Qwen3 4B → response

The model is not given unrestricted shell access.

## Requirements
Windows 10/11, Python 3.10+ (3.13 recommended), Ollama, and Qwen3 4B.

Install the model with: ollama pull qwen3:4b

## Run
1. Run setup.bat
2. Run run.bat

Direct commands include: open notepad, open calculator, system info, take screenshot, show my ip, list files, search web Python 3.13, read clipboard.

## Security boundary
Security features are for authorized CTFs, local labs, owned systems, and defensive analysis. AK does not expose unrestricted arbitrary exploitation or destructive actions.

## Repository
https://github.com/asakiran2307/AK
