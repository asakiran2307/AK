def listen_once(timeout=5):
    try:
        import speech_recognition as sr
    except ImportError:
        return None, "SpeechRecognition is not installed."
    r=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio=r.listen(source,timeout=timeout,phrase_time_limit=10)
        return r.recognize_google(audio), None
    except Exception as exc:
        return None, str(exc)
