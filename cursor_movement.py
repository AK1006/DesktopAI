"""
Cursor movement and scroll automation module for the AI Voice Assistant.

Provides voice-controlled cursor clicks and scrolling functionality.
This module is experimental and contains work-in-progress features.
"""

import pyautogui as pg

from utils import say, take_command


def cursor_click():
    """Handle cursor movement commands via voice input.

    Supports:
        - "youtube search": Click on YouTube search bar area
        - "chrome search": Click on Chrome search bar area
        - "scroll down": Scroll the page down

    Note:
        Click coordinates are hardcoded and may need adjustment
        based on screen resolution and window positioning.
    """
    say("Cursor movement mode activated")
    comm = take_command()

    if "youtube search" in comm:
        pg.sleep(1)
        pg.click(800, 150)
    elif "chrome search" in comm:
        pg.sleep(1)
        pg.click(900, 600)
    elif "scroll down" in comm:
        pg.sleep(1)
        pg.scroll(-100)


if __name__ == "__main__":
    # Demo: wait 5 seconds then scroll
    pg.sleep(5)
    pg.scroll(500, 0, 3)