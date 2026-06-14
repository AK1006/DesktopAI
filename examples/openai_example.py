"""
Example: Using the OpenAI API

This script demonstrates how to generate text using the OpenAI API.
It is a standalone example and not integrated into the main voice assistant.

Prerequisites:
    1. Set OPENAI_API_KEY in your .env file
    2. Install the openai package: pip install openai

Usage:
    python examples/openai_example.py
"""

from openai import OpenAI

from config import OPENAI_API_KEY


def main():
    """Send a sample prompt to the OpenAI API and print the response."""
    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY is not set.")
        print("Please set it in your .env file. See .env.example for reference.")
        return

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Write an email to my boss for resignation."}
        ],
        temperature=1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
