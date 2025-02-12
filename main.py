import keyboard
import pyperclip
import time
import tkinter as tk
import os

user = os.path.expanduser('~')
config_file_path = os.path.join(user, 'Documents') + '/PortaRegistoConfig.txt'

max_copies_const: str = 'copias_maximas_guardadas'
label_width_const: str = 'ancho_caja_texto'
label_height_const: str = 'alto_caja_texto'
label_selected_background = 'color_fondo_texto_seleccionado'
label_unselected_background = 'color_fondo_texto_no_seleccionado'
keys_combo = 'combinacion_para_mostrar_panel(ej: ctrl+alt+v)'

config_dict: dict = {}


def read_config_file():
    global config_file_path
    global config_dict
    file = open(config_file_path, 'r')
    line = file.readline().strip()
    count: int = 0

    while (line):
        key, value = line.split('=')
        
        if (count < 3):
            value = int(value)

        config_dict[key] = value
        count += 1
        line = file.readline().strip()
    file.close()



def create_config_file():
    global config_file_path
    if (os.path.exists(config_file_path)):
        read_config_file()
        return
    
    with open(config_file_path, 'w') as file:
        file.write(f'{max_copies_const}=5\n')
        file.write(f'{label_width_const}=35\n')
        file.write(f'{label_height_const}=2\n')
        file.write(f'{label_selected_background}=#23272e\n')
        file.write(f'{label_unselected_background}=#333333\n')
        file.write(f'{keys_combo}=ctrl+alt+v\n')
    file.close()

create_config_file()
before_copies: list[str] = []
max_copies: int = config_dict[max_copies_const]
selection: int = 0


def get_paperclip() -> None:
    time.sleep(0.5)  # Esperar para que se copie primero en el portapapeles
    content: str = pyperclip.paste()

    # Verificar si la lista ya está llena
    if (len(before_copies) == max_copies):
        before_copies.pop(0)

    before_copies.append(content)

# Función para mover la selección hacia arriba
def move_selection_up(event=None) -> None:
    global selection
    selection -= 1
    if (selection < 0):
        selection = len(before_copies) - 1
    update_labels()

# Función para mover la selección hacia abajo
def move_selection_down(event=None) -> None:
    global selection
    selection += 1
    if (selection >= len(before_copies)):
        selection = 0
    update_labels()


# Función para pegar la selección actual
def paste_selection(event=None) -> None:
    if (before_copies):
        selected_text = before_copies[selection]
        root.clipboard_clear()
        root.clipboard_append(selected_text)
        root.update()
    root.destroy()
    keyboard.write(selected_text)

def update_labels() -> None:
    for widget in root.winfo_children():
        widget.destroy()  # Limpiar los widgets anteriores

    for index, text in enumerate(before_copies):
        label = tk.Label(root, text=text, justify='center', width=config_dict[label_width_const], height=config_dict[label_height_const], fg='white')
        if (index == selection):
            label.config(bg=config_dict[label_selected_background])
        else:
            label.config(bg=config_dict[label_unselected_background])
        label.pack()

def show_before_copies() -> None:
    global root
    root = tk.Tk()
    root.title("Seleccionar texto copiado")
    root.config(bg="#23272e")
    root.attributes('-topmost', True)
    update_labels()  # Actualizar las etiquetas al abrir la ventana
    root.bind('<Up>', move_selection_up)
    root.bind('<Down>', move_selection_down)
    root.bind('<Return>', paste_selection)
    
    root.focus_get()
    root.mainloop()

keyboard.add_hotkey("ctrl+c", get_paperclip)
keyboard.add_hotkey(config_dict[keys_combo], show_before_copies)

keyboard.wait('esc')