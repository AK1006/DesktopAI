"""
Ameeca — AI Voice Assistant

A Windows-based voice-controlled assistant that can open/close applications,
browse websites, tell time, send WhatsApp messages, play music, and more.

Usage:
    python main.py
"""

import os
import webbrowser
import datetime
import subprocess
import pyautogui
import time

from utils import say, take_command


def wishme():
    """Greet the user based on the current time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 12:
        say("Good Morning ma'am!")
    elif hour >= 12 and hour < 16:
        say("Good Afternoon ma'am!")
    else:
        say("Good Evening ma'am!")


def open_application(app_open_command):
    """Open a Windows application using the given system command.

    Args:
        app_open_command (str): The system command to launch the application.
    """
    os.system(app_open_command)


def close_application(app_command):
    """Close a running Windows application by its process name.

    Includes safeguards against closing critical system processes.

    Args:
        app_command (str): The command/process name used to launch the application.
    """
    if "start" in app_command:
        say("Sorry, no close command available for this app.")
        return

    # Extract the .exe name (process name)
    app_name = app_command.split()[0]

    critical_processes = [
        "explorer.exe", "svchost.exe", "winlogon.exe", "csrss.exe",
        "lsass.exe", "taskhostw.exe", "dwm.exe", "smss.exe", "services.exe"
    ]

    # Safeguard: Prevent closing system app that might affect system if closed
    if app_name in critical_processes:
        say(f"Terminating {app_name} is not allowed as it is critical to system stability.")
        return

    # Check if the app is running using tasklist
    try:
        result = subprocess.check_output(f'tasklist | findstr /i {app_name}', shell=True)
        if app_name.lower() in result.decode().lower():
            # Close the app using taskkill
            os.system(f'taskkill /IM {app_name} /F')
            say(f"{app_name} has been closed.")
        else:
            say(f"{app_name} is not running.")
    except subprocess.CalledProcessError:
        say(f"{app_name} is not running or has already ended.")


def alt_tab_switch():
    """Simulate an Alt+Tab key press to switch between windows."""
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.5)  # Pause to allow the Alt+Tab UI to pop up
    pyautogui.keyUp('alt')


if __name__ == "__main__":
    print("Hello!")
    wishme()
    say("I am Ameeca, how can I help you?")

    # List of apps with their open commands
    apps = [
        ["calculator", "calc.exe"],
        ["camera", "start microsoft.windows.camera:"],
        ["notepad", "notepad.exe"],
        ["paint", "mspaint.exe"],
        ["wordpad", "write.exe"],
        ["command prompt", "cmd.exe"],
        ["file explorer", "explorer.exe"],
        ["settings", "start ms-settings:"],
        ["task manager", "taskmgr.exe"],
        ["control panel", "control.exe"],
        ["powershell", "powershell.exe"],
        ["edge", "start microsoft-edge:"],
        ["store", "start ms-windows-store:"],
        ["outlook", "start outlook.exe"],
        ["word", "start winword.exe"],
        ["excel", "start excel.exe"],
        ["powerpoint", "start powerpnt.exe"],
        ["onenote", "start onenote.exe"],
        ["snipping tool", "SnippingTool.exe"],
        ["note", "start ONENOTE.EXE"],
    ]

    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["chat gpt", "https://chatgpt.com"],
        ["instagram", "https://www.instagram.com"],
        ["google", "https://www.google.com"],
    ]

    while True:
        try:
            print("Listening....")
            query = take_command()
            print("Recognizing....")

            # Check for exit commands
            if any(cmd in query.lower() for cmd in ["exit", "quit", "stop", "goodbye"]):
                say("Goodbye ma'am! Have a great day!")
                break

            # Open websites
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"Opening {site[0]} ma'am....")
                    webbrowser.open(site[1])

            # Open or close applications
            for app in apps:
                if f"open {app[0]}".lower() in query.lower():
                    say(f"Opening {app[0]} ma'am")
                    open_application(app[1])
                elif f"close {app[0]}".lower() in query.lower():
                    say(f"Closing {app[0]} ma'am")
                    close_application(app[1])

            # Special case: close Calculator (UWP app)
            if "close calculator" in query.lower():
                say("Closing Calculator app using PowerShell")
                os.system(
                    'powershell -Command "Get-Process | Where-Object '
                    "{ $_.ProcessName -eq 'CalculatorApp' } | Stop-Process\""
                )

            # Tell the time
            if "the time" in query.lower():
                strf_time = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Ma'am the time is {strf_time}")

            # Type text
            if "write" in query.lower():
                pyautogui.write(query.replace("write", ""), 0.1)

            # Press Enter key
            if "enter" in query.lower():
                pyautogui.press('enter')

            # Switch windows (Alt+Tab)
            if "switch" in query.lower():
                alt_tab_switch()

            # Send WhatsApp message
            if "whatsapp" in query.lower():
                from whatsapp_msg import whatsapp
                whatsapp()

            # Play music on YouTube
            if "music" in query.lower():
                from youtube import music
                music()

            # Control YouTube video
            if "video" in query.lower():
                from youtube import youtube_auto
                youtube_auto()

        except KeyboardInterrupt:
            say("Goodbye ma'am!")
            break
        except Exception as e:
            print(f"Error: {e}")
            say("Sorry, something went wrong. Please try again.")
