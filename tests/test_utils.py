"""
Unit tests for the shared utility functions (utils.py).

These tests mock hardware-dependent components (microphone, TTS engine)
to verify logic without requiring physical devices.
"""

import unittest
from unittest.mock import patch, MagicMock


class TestSayFunction(unittest.TestCase):
    """Tests for the say() text-to-speech function."""

    @patch('utils.pyttsx3')
    def test_say_calls_engine_with_text(self, mock_pyttsx3):
        """Verify that say() initializes the engine, sets voice, and speaks."""
        from utils import say

        mock_engine = MagicMock()
        mock_voice = MagicMock()
        mock_voice.id = "test_voice_id"
        mock_engine.getProperty.return_value = [MagicMock(), mock_voice]
        mock_pyttsx3.init.return_value = mock_engine

        say("Hello world")

        mock_pyttsx3.init.assert_called_once_with('sapi5')
        mock_engine.getProperty.assert_called_once_with('voices')
        mock_engine.setProperty.assert_called_once_with('voice', 'test_voice_id')
        mock_engine.say.assert_called_once_with("Hello world")
        mock_engine.runAndWait.assert_called_once()

    @patch('utils.pyttsx3')
    def test_say_with_empty_string(self, mock_pyttsx3):
        """Verify that say() handles empty strings without crashing."""
        from utils import say

        mock_engine = MagicMock()
        mock_voice = MagicMock()
        mock_voice.id = "test_voice_id"
        mock_engine.getProperty.return_value = [MagicMock(), mock_voice]
        mock_pyttsx3.init.return_value = mock_engine

        say("")

        mock_engine.say.assert_called_once_with("")
        mock_engine.runAndWait.assert_called_once()


class TestTakeCommandFunction(unittest.TestCase):
    """Tests for the take_command() voice recognition function."""

    @patch('utils.sr.Microphone')
    @patch('utils.sr.Recognizer')
    def test_take_command_returns_recognized_text(self, mock_recognizer_class, mock_mic):
        """Verify successful speech recognition returns the recognized text."""
        from utils import take_command

        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_recognizer.recognize_google.return_value = "open notepad"

        result = take_command()

        self.assertEqual(result, "open notepad")
        mock_recognizer.recognize_google.assert_called_once()

    @patch('utils.sr.Microphone')
    @patch('utils.sr.Recognizer')
    def test_take_command_returns_error_on_exception(self, mock_recognizer_class, mock_mic):
        """Verify that recognition failure returns an error message."""
        from utils import take_command

        mock_recognizer = MagicMock()
        mock_recognizer_class.return_value = mock_recognizer
        mock_recognizer.recognize_google.side_effect = Exception("API error")

        result = take_command()

        self.assertIn("sorry", result.lower())


if __name__ == "__main__":
    unittest.main()
