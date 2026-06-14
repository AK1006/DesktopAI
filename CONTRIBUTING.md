# Contributing to Ameeca — AI Voice Assistant

Thank you for your interest in contributing to **Ameeca**! Whether you're reporting a bug, suggesting a feature, or submitting a pull request, your help is welcome and appreciated.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Report Bugs](#how-to-report-bugs)
- [How to Suggest Features](#how-to-suggest-features)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please be kind, constructive, and professional in all interactions. Harassment, discrimination, or abusive behavior of any kind will not be tolerated.

---

## How to Report Bugs

If you encounter a bug, please [open an issue](../../issues/new) and include:

1. **Summary** — A clear, concise description of the problem.
2. **Steps to Reproduce** — Numbered steps to reliably trigger the bug.
3. **Expected Behavior** — What you expected to happen.
4. **Actual Behavior** — What actually happened, including any error messages or tracebacks.
5. **Environment Details**:
   - Operating system and version (e.g., Windows 11 23H2)
   - Python version (`python --version`)
   - Microphone hardware / driver info (if audio-related)
6. **Screenshots or Logs** — Attach any relevant output, if applicable.

> **Tip:** The more detail you provide, the faster we can diagnose and fix the issue.

---

## How to Suggest Features

We'd love to hear your ideas! To propose a new feature:

1. [Open an issue](../../issues/new) with the title prefixed by `[Feature Request]`.
2. Describe the feature and the problem it solves.
3. Provide example use cases or voice commands, if applicable.
4. Note any alternative approaches you've considered.

Feature requests that align with the project's goal of being a hands-free, voice-controlled desktop assistant will be prioritized.

---

## Development Setup

### Prerequisites

| Requirement       | Minimum Version |
|-------------------|-----------------|
| Operating System  | Windows 10      |
| Python            | 3.10+           |
| Microphone        | Any working USB / built-in mic |
| Internet          | Required for speech recognition |

### Getting Started

```bash
# 1. Fork and clone the repository
git clone https://github.com/<your-username>/pythonProject_AI_Assistant.git
cd pythonProject_AI_Assistant

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
copy .env.example .env
# Edit .env and add your API keys

# 5. Run the assistant
python main.py
```

### Running Tests

```bash
pip install pytest
pytest
```

---

## Code Style Guidelines

This project follows **PEP 8** — the Python style guide. Please adhere to these conventions:

### General Rules

| Rule                        | Standard                                      |
|-----------------------------|-----------------------------------------------|
| Indentation                 | 4 spaces (no tabs)                            |
| Max line length             | 100 characters                                |
| String quotes               | Double quotes (`"`) preferred                 |
| Imports                     | Grouped: stdlib → third-party → local         |
| Trailing whitespace         | None                                          |
| Final newline               | Required at end of every file                 |

### Docstrings

All public functions and classes must include a **Google-style docstring**:

```python
def say(text):
    """Convert text to speech using the pyttsx3 SAPI5 engine.

    Args:
        text (str): The text to speak aloud.

    Returns:
        None
    """
```

### Naming Conventions

| Type       | Convention       | Example            |
|------------|------------------|--------------------|
| Functions  | `snake_case`     | `take_command()`   |
| Variables  | `snake_case`     | `app_name`         |
| Constants  | `UPPER_SNAKE`    | `ANTHROPIC_API_KEY`|
| Classes    | `PascalCase`     | `VoiceAssistant`   |
| Modules    | `snake_case`     | `whatsapp_msg.py`  |

### Linting

We recommend running a linter before submitting your code:

```bash
pip install flake8
flake8 --max-line-length=100 .
```

---

## Pull Request Process

1. **Fork** the repository and create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines above.

3. **Test** your changes thoroughly:
   - Ensure all existing tests pass (`pytest`).
   - Add new tests for any new functionality.
   - Manually test voice commands if modifying the assistant logic.

4. **Commit** with a clear, descriptive message:
   ```
   feat: add volume control voice command
   fix: correct microphone timeout handling
   docs: update README with new commands
   ```
   Use [Conventional Commits](https://www.conventionalcommits.org/) format when possible.

5. **Push** your branch and [open a Pull Request](../../pulls):
   - Provide a clear description of your changes.
   - Reference any related issues (e.g., `Closes #12`).
   - Include screenshots or demo recordings for UI/voice changes.

6. **Code Review** — A maintainer will review your PR. Please be responsive to feedback and make requested changes promptly.

### PR Checklist

Before submitting, verify:

- [ ] Code follows PEP 8 and project style guidelines
- [ ] All existing tests pass
- [ ] New features include appropriate tests
- [ ] Docstrings are added for new public functions
- [ ] No hardcoded API keys, phone numbers, or secrets
- [ ] `requirements.txt` is updated if new dependencies are added
- [ ] CHANGELOG.md is updated with your changes

---

## Questions?

If you have any questions about contributing, feel free to open a discussion or reach out by creating an issue. We're happy to help you get started!

---

Thank you for helping make Ameeca better! 🎙️
