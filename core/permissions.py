class PermissionDecision:
    def __init__(self, allowed, reason):
        self.allowed=allowed
        self.reason=reason

class PermissionManager:
    def check(self,risk,confirmed=False):
        if risk=="low": return PermissionDecision(True,"low risk")
        if confirmed: return PermissionDecision(True,"explicit confirmation")
        return PermissionDecision(False,f"{risk} risk requires confirmation")

    def confirm_console(self,description):
        answer=input(f"AK confirmation required for: {description}\nType YES to continue: ")
        return answer.strip().upper()=="YES"
