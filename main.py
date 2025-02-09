import keyboard
import pyperclip
import time


before_copies: list[str] = []
max_copies: int = 5
selection: int = 0


def get_paperclip() -> None:
    global record
    time.sleep(0.5) # Espero para que se copie primero en el portapapeles
    content: str = pyperclip.paste()
    
    # Veo si la lista ya está llena
    if (len(before_copies) == max_copies):
        before_copies.pop(0)

    before_copies.append(content)
    print('texto copiado')


def show_before_copies() -> None:
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

    print("Seleccion : ", selection)

def move_selection_up() -> None:
    global selection
    selection -= 1
    if (selection < 0):
        selection = 5
        
    print("Seleccion : ", selection)
    

    

keyboard.add_hotkey("ctrl+c", get_paperclip)
keyboard.add_hotkey("ctrl+alt+v", show_before_copies)
keyboard.add_hotkey("down", move_selection_down)
keyboard.add_hotkey("up", move_selection_up)


keyboard.wait('esc')
   