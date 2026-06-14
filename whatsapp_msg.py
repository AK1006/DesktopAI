"""
WhatsApp messaging module for the AI Voice Assistant.

Sends WhatsApp messages using pywhatkit based on voice commands.
Requires WHATSAPP_PHONE_NUMBER to be set in the .env file.
"""

import datetime
import time

import pyautogui
import pywhatkit

from config import WHATSAPP_PHONE_NUMBER
from utils import say, take_command


def whatsapp():
    """Send a WhatsApp message via voice command.

    Prompts the user for a recipient name and message content,
    then schedules the message to be sent 2 minutes from now.
    """
    say("Ma'am, tell me the name of the person")
    name = take_command()

    say("What message would you like to send?")
    msg = take_command()

    # Get current time and add 2 minutes to ensure message sends
    current_time = datetime.datetime.now()
    hour = current_time.hour
    mins = current_time.minute + 2

    # Handle case where minutes exceed 59
    if mins >= 60:
        hour += 1
        mins -= 60

    phone_number = WHATSAPP_PHONE_NUMBER
    if not phone_number:
        say("WhatsApp phone number is not configured. Please set it in the .env file.")
        print("Error: WHATSAPP_PHONE_NUMBER not set in .env file.")
        return

    try:
        pywhatkit.sendwhatmsg(phone_number, msg, hour, mins, 20)
        say("Ok ma'am. Sending WhatsApp message!")
        time.sleep(5)
        pyautogui.press('enter')
    except Exception as e:
        say("Sorry ma'am, there was an error sending the message.")
        print(f"Error: {e}")


if __name__ == "__main__":
    whatsapp()