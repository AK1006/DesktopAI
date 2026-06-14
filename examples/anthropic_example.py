"""
Example: Using the Anthropic Claude API

This script demonstrates how to generate text using the Anthropic Claude API.
It is a standalone example and not integrated into the main voice assistant.

Prerequisites:
    1. Set ANTHROPIC_API_KEY in your .env file
    2. Install the anthropic package: pip install anthropic

Usage:
    python examples/anthropic_example.py
"""

import anthropic

from config import ANTHROPIC_API_KEY


def main():
    """Send a sample prompt to the Anthropic Claude API and print the response."""
    if not ANTHROPIC_API_KEY:
        print("Error: ANTHROPIC_API_KEY is not set.")
        print("Please set it in your .env file. See .env.example for reference.")
        return

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": "Generate an email to my boss for sick leave."}
        ]
    )
    print(message.content)


if __name__ == "__main__":
    main()
