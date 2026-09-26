class PermissionManager:
    CONFIRM_WORDS = {"delete", "remove", "shutdown", "restart", "format", "kill", "send", "execute"}

    def needs_confirmation(self, text):
        t = text.lower()
        return any(word in t for word in self.CONFIRM_WORDS)

    def confirm(self, action):
        answer = input(f"AK confirmation required for: {action}\nType YES to continue: ")
        return answer.strip().upper() == "YES"
