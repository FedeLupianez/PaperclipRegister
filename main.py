import keyboard
import pyperclip
import time
import tkinter as tk


before_copies: list[str] = []
max_copies: int = 5
selection: int = 0


def get_paperclip() -> None:
    time.sleep(0.5) # Espero para que se copie primero en el portapapeles
    content: str = pyperclip.paste()
    
    # Veo si la lista ya está llena
    if (len(before_copies) == max_copies):
        before_copies.pop(0)

    before_copies.append(content)
    print('texto copiado')


def show_before_copies() -> None:
    global is_selection_activate
    is_selection_activate = True
    print('---------------------------')
    for index in range(len(before_copies)):
        if (index == selection): 
            print('@', end='')
        print(before_copies[index])
        

def move_selection_down() -> None:
    global selection
    selection += 1    
    if (selection > 5):
        selection = 0


def move_selection_up() -> None:
    global selection
    selection -= 1
    if (selection < 0):
        selection = 5


def paste_selection() -> None:
    global is_selection_activate
    if (not is_selection_activate):
        return

    keyboard.write(before_copies[selection])
    is_selection_activate = False


keyboard.add_hotkey("ctrl+c", get_paperclip)
keyboard.add_hotkey("ctrl+alt+v", show_before_copies)
keyboard.add_hotkey("down", move_selection_down)
keyboard.add_hotkey("up", move_selection_up)
keyboard.add_hotkey("enter", paste_selection)


keyboard.wait('esc')
   