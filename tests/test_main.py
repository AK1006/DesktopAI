"""
Unit tests for the main voice assistant module (main.py).

Tests core logic functions: wishme(), open_application(), close_application(),
and alt_tab_switch(). All system/hardware interactions are mocked.
"""

import unittest
from unittest.mock import patch, MagicMock
import datetime


class TestWishmeFunction(unittest.TestCase):
    """Tests for the wishme() greeting function."""

    @patch('main.say')
    @patch('main.datetime')
    def test_wishme_morning(self, mock_datetime, mock_say):
        """Verify morning greeting between 3:00 and 11:59."""
        mock_now = MagicMock()
        mock_now.hour = 8
        mock_datetime.datetime.now.return_value = mock_now

        from main import wishme
        wishme()

        mock_say.assert_called_once_with("Good Morning ma'am!")

    @patch('main.say')
    @patch('main.datetime')
    def test_wishme_afternoon(self, mock_datetime, mock_say):
        """Verify afternoon greeting between 12:00 and 15:59."""
        mock_now = MagicMock()
        mock_now.hour = 14
        mock_datetime.datetime.now.return_value = mock_now

        from main import wishme
        wishme()

        mock_say.assert_called_once_with("Good Afternoon ma'am!")

    @patch('main.say')
    @patch('main.datetime')
    def test_wishme_evening(self, mock_datetime, mock_say):
        """Verify evening greeting after 16:00 or before 3:00."""
        mock_now = MagicMock()
        mock_now.hour = 20
        mock_datetime.datetime.now.return_value = mock_now

        from main import wishme
        wishme()

        mock_say.assert_called_once_with("Good Evening ma'am!")


class TestOpenApplication(unittest.TestCase):
    """Tests for the open_application() function."""

    @patch('main.os.system')
    def test_open_application_calls_os_system(self, mock_system):
        """Verify that open_application passes the command to os.system."""
        from main import open_application
        open_application("notepad.exe")
        mock_system.assert_called_once_with("notepad.exe")


class TestCloseApplication(unittest.TestCase):
    """Tests for the close_application() function."""

    @patch('main.say')
    def test_close_application_rejects_start_command(self, mock_say):
        """Verify that apps launched with 'start' cannot be closed."""
        from main import close_application
        close_application("start microsoft.windows.camera:")
        mock_say.assert_called_once_with("Sorry, no close command available for this app.")

    @patch('main.say')
    def test_close_application_blocks_critical_process(self, mock_say):
        """Verify that critical system processes cannot be terminated."""
        from main import close_application
        close_application("explorer.exe")
        self.assertIn("not allowed", mock_say.call_args[0][0])

    @patch('main.os.system')
    @patch('main.subprocess.check_output')
    @patch('main.say')
    def test_close_application_kills_running_app(self, mock_say, mock_check, mock_system):
        """Verify that a running non-critical app is terminated with taskkill."""
        mock_check.return_value = b"notepad.exe  12345 Console  1  10,000 K"

        from main import close_application
        close_application("notepad.exe")

        mock_system.assert_called_once_with("taskkill /IM notepad.exe /F")


class TestAltTabSwitch(unittest.TestCase):
    """Tests for the alt_tab_switch() function."""

    @patch('main.time.sleep')
    @patch('main.pyautogui')
    def test_alt_tab_switch_sequence(self, mock_pyautogui, mock_sleep):
        """Verify correct key sequence: Alt down → Tab → pause → Alt up."""
        from main import alt_tab_switch
        alt_tab_switch()

        mock_pyautogui.keyDown.assert_called_once_with('alt')
        mock_pyautogui.press.assert_called_once_with('tab')
        mock_sleep.assert_called_once_with(0.5)
        mock_pyautogui.keyUp.assert_called_once_with('alt')


if __name__ == "__main__":
    unittest.main()
