import keyboard
import pyperclip
import time
import tkinter as tk


before_copies: list[str] = []
max_copies: int = 5
selection: int = 0


def get_paperclip() -> None:
    time.sleep(0.5)  # Esperar para que se copie primero en el portapapeles
    content: str = pyperclip.paste()

    # Verificar si la lista ya está llena
    if len(before_copies) == max_copies:
        before_copies.pop(0)

    before_copies.append(content)
    print('Texto copiado')

# Función para mover la selección hacia arriba


def move_selection_up(event=None) -> None:
    global selection
    selection -= 1
    if selection < 0:
        selection = len(before_copies) - 1
    update_labels()


# Función para mover la selección hacia abajo
def move_selection_down(event=None) -> None:
    global selection
    selection += 1
    if selection >= len(before_copies):
        selection = 0
    update_labels()


# Función para pegar la selección actual
def paste_selection(event=None) -> None:
    if before_copies:
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
        label = tk.Label(root, text=text, justify='center', width=50, height=2, fg='white')
        if index == selection:
            label.config(bg="#23272e")
        else:
            label.config(bg="#333333")
        label.pack()


def show_before_copies() -> None:
    global root
    root = tk.Tk()
    root.title("Seleccionar texto copiado")
    root.config(bg="#23272e", takefocus=True)
    root.attributes('-topmost', True)

    root.bind('<Up>', move_selection_up)
    root.bind('<Down>', move_selection_down)
    root.bind('<Return>', paste_selection)

    update_labels()  # Actualizar las etiquetas al abrir la ventana
    root.mainloop()


keyboard.add_hotkey("ctrl+c", get_paperclip)
keyboard.add_hotkey("ctrl+alt+v", show_before_copies)

keyboard.wait('esc')