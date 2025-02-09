import keyboard
import pyperclip
import time


def get_paperclip() -> None:
    content: str = pyperclip.paste()
    print('contenido : ', content)


keyboard.add_hotkey("ctrl+c", get_paperclip)

while (True):
    try : 
        time.sleep(1)
    except (KeyboardInterrupt):
        pass
    