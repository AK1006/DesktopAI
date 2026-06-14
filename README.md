<p align="center">
  <h1 align="center">🎙️ Ameeca — AI Voice Assistant</h1>
  <p align="center">
    A Windows-based AI-powered voice assistant built with Python.<br/>
    Control your desktop, browse the web, send messages, and play music — all hands-free.
  </p>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#voice-commands-reference">Commands</a> •
  <a href="#troubleshooting">Troubleshooting</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## About

**Ameeca** is a voice-controlled desktop assistant that listens for spoken commands and performs actions on your Windows PC. Powered by Google Speech Recognition and Python's text-to-speech engine (SAPI5), Ameeca can open and close applications, navigate to websites, tell you the time, send WhatsApp messages, play YouTube music, control video playback, type text, and more — entirely through voice interaction.

---

## Features

- 🎙️ **Voice-Controlled Interface** — Hands-free operation with Google Speech Recognition
- 🖥️ **Open & Close Applications** — Calculator, Notepad, Edge, Paint, WordPad, Task Manager, and more
- 🌐 **Open Websites** — YouTube, Wikipedia, Google, Instagram, ChatGPT
- ⏰ **Tell Current Time** — Ask Ameeca for the time and hear it spoken aloud
- 💬 **Send WhatsApp Messages** — Dictate and send messages via WhatsApp Web
- 🎵 **Play Music on YouTube** — Request any song and Ameeca plays it
- 🎬 **Control YouTube Playback** — Pause, skip, mute, fullscreen — all by voice
- ⌨️ **Type Text & Simulate Keyboard** — Dictate text and press Enter hands-free
- 🔄 **Switch Between Windows** — Alt+Tab window switching via voice command

---

## Tech Stack

| Component            | Technology                          |
|----------------------|-------------------------------------|
| Language             | Python 3.10+                        |
| Speech Recognition   | `SpeechRecognition` (Google API)    |
| Text-to-Speech       | `pyttsx3` (Windows SAPI5)           |
| GUI Automation       | `pyautogui`                         |
| WhatsApp Messaging   | `pywhatkit`                         |
| Keyboard Control     | `keyboard`                          |
| Windows Integration  | `pypiwin32` (`win32com`, `win32gui`)|
| Configuration        | `python-dotenv`                     |
| AI APIs (examples)   | `anthropic`, `openai`               |

---

## Prerequisites

| Requirement         | Details                              |
|---------------------|--------------------------------------|
| Operating System    | Windows 10 / 11                      |
| Python              | 3.10 or higher                       |
| Microphone          | Any working microphone               |
| Internet Connection | Required for speech recognition & web features |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/pythonProject_AI_Assistant.git
cd pythonProject_AI_Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
copy .env.example .env
```

Open `.env` in your editor and fill in your values:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
WHATSAPP_PHONE_NUMBER=+1234567890
```

### 6. Run the Assistant

```bash
python main.py
```

Ameeca will greet you and start listening for commands. 🎙️

---

## Voice Commands Reference

| Command                        | Action                                      |
|--------------------------------|---------------------------------------------|
| `"Open [app name]"`           | Opens a Windows application                 |
| `"Close [app name]"`          | Closes a running application                |
| `"Open YouTube/Google/etc."`  | Opens website in default browser            |
| `"The time"`                  | Tells the current time                      |
| `"WhatsApp"`                  | Starts the WhatsApp message flow            |
| `"Music"`                     | Play a song on YouTube                      |
| `"Video"`                     | Control YouTube video playback              |
| `"Write [text]"`              | Types the specified text                    |
| `"Enter"`                     | Presses the Enter key                       |
| `"Switch"`                    | Alt+Tab to switch windows                   |
| `"Exit"` / `"Quit"` / `"Stop"` / `"Goodbye"` | Exit the assistant       |

---

## Supported Applications

Ameeca can open and close the following Windows applications by voice:

| Voice Command       | Application           | System Command             |
|---------------------|-----------------------|----------------------------|
| `"Calculator"`      | Calculator            | `calc.exe`                 |
| `"Camera"`          | Camera                | `start microsoft.windows.camera:` |
| `"Notepad"`         | Notepad               | `notepad.exe`              |
| `"Paint"`           | Microsoft Paint       | `mspaint.exe`              |
| `"WordPad"`         | WordPad               | `write.exe`                |
| `"Command Prompt"`  | Command Prompt        | `cmd.exe`                  |
| `"File Explorer"`   | File Explorer         | `explorer.exe`             |
| `"Settings"`        | Windows Settings      | `start ms-settings:`       |
| `"Task Manager"`    | Task Manager          | `taskmgr.exe`              |
| `"Control Panel"`   | Control Panel         | `control.exe`              |
| `"PowerShell"`      | Windows PowerShell    | `powershell.exe`           |
| `"Edge"`            | Microsoft Edge        | `start microsoft-edge:`    |
| `"Store"`           | Microsoft Store       | `start ms-windows-store:`  |
| `"Outlook"`         | Microsoft Outlook     | `start outlook.exe`        |
| `"Word"`            | Microsoft Word        | `start winword.exe`        |
| `"Excel"`           | Microsoft Excel       | `start excel.exe`          |
| `"PowerPoint"`      | Microsoft PowerPoint  | `start powerpnt.exe`       |
| `"OneNote"`         | Microsoft OneNote     | `start onenote.exe`        |
| `"Snipping Tool"`   | Snipping Tool         | `SnippingTool.exe`         |
| `"Note"`            | OneNote (quick note)  | `start ONENOTE.EXE`        |

### Supported Websites

| Voice Command        | URL                              |
|----------------------|----------------------------------|
| `"Open YouTube"`     | https://www.youtube.com          |
| `"Open Wikipedia"`   | https://www.wikipedia.com        |
| `"Open Chat GPT"`    | https://chatgpt.com              |
| `"Open Instagram"`   | https://www.instagram.com        |
| `"Open Google"`      | https://www.google.com           |

---

## Configuration

Ameeca uses a `.env` file for sensitive configuration. Copy the provided template and fill in your values:

```bash
copy .env.example .env
```

### Environment Variables

| Variable                | Description                                      | Required |
|-------------------------|--------------------------------------------------|----------|
| `ANTHROPIC_API_KEY`     | API key for Anthropic Claude (example scripts)    | Optional |
| `OPENAI_API_KEY`        | API key for OpenAI GPT (example scripts)          | Optional |
| `WHATSAPP_PHONE_NUMBER` | Phone number with country code for WhatsApp       | For WhatsApp feature |

> **⚠️ Important:** Never commit your `.env` file to version control. It is already included in `.gitignore`.

---

## Project Structure

```
pythonProject_AI_Assistant/
├── main.py              # Main assistant entry point and command loop
├── utils.py             # Shared utilities (TTS, speech recognition)
├── config.py            # Environment variable configuration loader
├── whatsapp_msg.py      # WhatsApp messaging functionality
├── youtube.py           # YouTube music & video control
├── cursor_movement.py   # Cursor/mouse movement utilities
├── Anthropic.py         # Example: Anthropic Claude API usage
├── Openaitest.py        # Example: OpenAI GPT API usage
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation (this file)
├── LICENSE              # MIT License
├── CONTRIBUTING.md      # Contribution guidelines
└── CHANGELOG.md         # Version history and release notes
```

---

## Examples

The project includes example scripts demonstrating AI API integration:

- **`Anthropic.py`** — Demonstrates how to call the Anthropic Claude API for conversational AI responses.
- **`Openaitest.py`** — Demonstrates how to use the OpenAI GPT API for text generation.

To run the examples, ensure the corresponding API key is set in your `.env` file:

```bash
# Run the Anthropic example
python Anthropic.py

# Run the OpenAI example
python Openaitest.py
```

> These scripts are provided as reference implementations and are not required for the core voice assistant functionality.

---

## Troubleshooting

### 🎤 Microphone Not Detected

- Ensure your microphone is plugged in and set as the default input device.
- Check Windows Settings → System → Sound → Input.
- Try running: `python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"` to verify detection.

### 🗣️ Speech Not Recognized

- Speak clearly and at a moderate pace.
- Reduce background noise.
- Ensure you have an active internet connection (Google Speech API requires it).
- If recognition consistently fails, check your microphone sensitivity in Windows Sound settings.

### 🔊 pyttsx3 Voice Not Found

- Ameeca uses `voices[1]` (typically the female voice). If your system has only one voice installed, change the index to `0` in `utils.py` and `main.py`.
- Install additional Windows TTS voices: Settings → Time & Language → Speech → Manage voices.

### 💬 WhatsApp Message Not Sending

- Ensure WhatsApp Web is logged in on your default browser.
- The `pywhatkit` library requires a brief delay to load WhatsApp Web — do not interact with the browser during the sending process.
- Verify the phone number format in `.env` includes the country code (e.g., `+11234567890`).

### 🔒 Permission Errors for Keyboard Module

- The `keyboard` module requires administrator privileges on Windows.
- Run your terminal or IDE as **Administrator**.
- Alternatively, right-click `main.py` → Run as Administrator.

### ⚙️ pyautogui Fails to Type or Press Keys

- Ensure no other application is intercepting keyboard input.
- Some secure applications (e.g., banking apps, UAC prompts) block programmatic keyboard input.

---

## Future Improvements

- 🧠 **AI-Powered Natural Language Understanding** — Integrate LLMs for more natural, conversational interactions
- 🔔 **Custom Wake Word Detection** — "Hey Ameeca" activation without constant listening
- 🐧 **Cross-Platform Support** — Extend to macOS and Linux
- 🖼️ **GUI Interface** — Visual dashboard with command history and status indicators
- 🔌 **Plugin System** — Extensible architecture for community-built modules
- 💾 **Conversation Memory** — Remember context across sessions for smarter responses
- 📅 **Calendar & Reminders** — Voice-activated scheduling and reminders
- 🏠 **Smart Home Integration** — Control IoT devices via voice commands

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before getting started.

---

## Acknowledgments

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — Google Speech Recognition API wrapper
- [pyttsx3](https://pypi.org/project/pyttsx3/) — Offline text-to-speech engine
- [pyautogui](https://pypi.org/project/PyAutoGUI/) — GUI automation toolkit
- [pywhatkit](https://pypi.org/project/pywhatkit/) — WhatsApp and YouTube automation
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management

---

<p align="center">
  Made with ❤️ by <strong>Amisha Karke</strong>
</p>
