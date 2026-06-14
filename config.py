"""
Configuration module for the AI Voice Assistant.

Loads API keys and sensitive configuration from environment variables.
Copy `.env.example` to `.env` and fill in your values before running.
"""

import os

from dotenv import load_dotenv

load_dotenv()

# API Keys (loaded from environment variables)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# WhatsApp configuration
WHATSAPP_PHONE_NUMBER = os.environ.get("WHATSAPP_PHONE_NUMBER", "")