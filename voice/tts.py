def speak(text):
    try:
        import pyttsx3
    except ImportError:
        return False, "pyttsx3 is not installed."
    try:
        engine=pyttsx3.init(); engine.say(text); engine.runAndWait(); return True, None
    except Exception as exc:
        return False, str(exc)
