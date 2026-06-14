"""
Shared utility functions for the AI Voice Assistant.

Provides common text-to-speech and voice recognition functionality
used across all modules.
"""

import speech_recognition as sr
import pyttsx3


def say(text):
    """Convert text to speech using the pyttsx3 SAPI5 engine.

    Args:
        text (str): The text to speak aloud.
    """
    speaker = pyttsx3.init('sapi5')
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say(text)
    speaker.runAndWait()


def take_command():
    """Listen for a voice command via the microphone and return the recognized text.

    Uses Google's Speech Recognition API with Indian English locale.

    Returns:
        str: The recognized voice command, or an error message if recognition fails.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print("User said:", query)
            return query
        except Exception:
            return "sorry error occurred, speak again!"
