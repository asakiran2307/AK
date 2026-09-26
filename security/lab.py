from dataclasses import dataclass

@dataclass
class LabScope:
    target: str
    authorization: str

def scope_message(scope: LabScope | None = None):
    if not scope:
        return "Security mode requires an explicit authorized lab scope."
    return f"Authorized scope: {scope.target} | {scope.authorization}"
