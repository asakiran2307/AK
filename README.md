# AK — Local JARVIS AI Assistant

AK is a local-first Windows desktop assistant built around **Qwen3 4B + Ollama**.

## Core architecture

Voice/Text → Intent → Qwen3 → Planner → Permission Layer → Tools → Result → Qwen3 → UI/TTS

## Included foundation

- Qwen3 4B through local Ollama
- Natural-language command routing
- Windows application launching
- System information
- Safe PowerShell execution with confirmation
- File operations
- Web opening/search
- SQLite conversation memory
- Optional voice input/output hooks
- Authorized security-lab command hooks
- Dark desktop dashboard
- Model/runtime health checks
- One-click Windows setup/run scripts

## Requirements

- Windows 10/11
- Python 3.13
- Ollama
- Qwen3 4B: `ollama pull qwen3:4b`

## Start

Run:

```bat
setup.bat
run.bat
```

If Ollama reports that `llama-server.exe` is missing, reinstall Ollama from its official installer before running AK.

## Security boundary

Security tooling is intended for systems, CTFs, labs, and infrastructure you are authorized to test. Destructive or high-impact actions require confirmation and are not exposed as unrestricted LLM shell execution.

## Project name

**AK**
