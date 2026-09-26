# AK Security Model

AK uses a tool boundary between the language model and the operating system.

Rules:
- Do not execute arbitrary shell commands from model output.
- Consequential tools require permission checks.
- Do not store secrets in logs.
- Security workflows require an explicitly authorized scope.
- Use security tools only on systems, labs, CTFs, or infrastructure where testing is authorized.