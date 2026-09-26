# Development

Run python doctor.py before development.

Unit tests: python -m unittest discover -s tests -v

Keep tools small and register them through core/registry.py. Prefer direct tools for deterministic commands and Qwen for reasoning-heavy tasks.