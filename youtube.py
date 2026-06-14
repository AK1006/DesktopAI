"""
YouTube music and video control module for the AI Voice Assistant.

Provides voice-controlled YouTube music playback and video controls
(pause, skip, mute, fullscreen, etc.) using keyboard simulation.
"""

import keyboard
import pywhatkit

from utils import say, take_command


def music():
    """Play a song on YouTube based on a voice command.

    Prompts the user for a song name and plays it using pywhatkit.
    """
    say("Tell me the name of the song ma'am")
    music_name = take_command()
    pywhatkit.playonyt(music_name)
    say("Your song is starting, enjoy!")


def youtube_auto():
    """Control YouTube video playback using voice commands.

    Supports: pause, restart, mute, skip, back, full screen, film mode.
    """
    say("What can I do for you ma'am?")
    comm = take_command()

    if 'pause' in comm:
        keyboard.press('space')
        say("Video paused")

    elif 'restart' in comm:
        say("Restarting the video")
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        say("Switching to full screen mode")
        keyboard.press('f')

    elif 'film mode' in comm:
        keyboard.press('t')

    say("Done ma'am")


if __name__ == "__main__":
    youtube_auto()
