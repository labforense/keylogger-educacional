import logging
import os
import tempfile
import unittest

import keylogger
from pynput import keyboard


class KeyloggerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.log_path = os.path.join(self.temp_dir.name, "keys.log")
        keylogger.LOG_FILE = self.log_path
        self.root_logger = logging.getLogger()
        self.root_logger.handlers.clear()
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_ignored_keys_are_not_logged(self):
        for key in keylogger.IGNORAR:
            keylogger.on_press(key)

        with open(self.log_path, "r", encoding="utf-8") as file:
            self.assertEqual(file.read().strip(), "")

    def test_regular_keys_are_logged(self):
        key = keyboard.KeyCode.from_char("a")
        keylogger.on_press(key)

        with open(self.log_path, "r", encoding="utf-8") as file:
            content = file.read()
            self.assertIn("Key pressed: a", content)


if __name__ == "__main__":
    unittest.main()
