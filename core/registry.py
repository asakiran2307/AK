from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: Callable[..., Any]
    risk: str = "low"
    requires_confirmation: bool = False

class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def list(self) -> list[Tool]:
        return list(self._tools.values())

    def descriptions(self) -> str:
        return "\n".join(
            f"- {t.name}: {t.description} [risk={t.risk}]"
            for t in self._tools.values()
        )
