from core.audit import audit
from core.permissions import PermissionManager
from core.registry import ToolRegistry

class ToolExecutor:
    def __init__(self, registry: ToolRegistry, permissions: PermissionManager):
        self.registry = registry
        self.permissions = permissions

    def execute(self, name: str, confirmed: bool = False, **kwargs):
        tool = self.registry.get(name)
        if not tool:
            return f"Unknown tool: {name}"
        decision = self.permissions.check(tool.risk, confirmed)
        if not decision.allowed:
            return f"Confirmation required before I can use '{name}'."
        audit("tool=%s args=%r confirmed=%s", name, kwargs, confirmed)
        try:
            result = tool.handler(**kwargs)
            audit("tool=%s success", name)
            return result
        except Exception as exc:
            audit("tool=%s failure=%s", name, exc)
            return f"Tool '{name}' failed: {exc}"
