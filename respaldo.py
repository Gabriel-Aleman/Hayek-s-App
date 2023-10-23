import tkinter as tk
from datetime import datetime

# Función para actualizar la fecha y hora
def update_datetime():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime('Fecha: %Y-%m-%d')
    current_time = current_datetime.strftime('Hora: %H:%M:%S %p')

    date_label.config(text=current_date)
    time_label.config(text=current_time)

    root.after(1000, update_datetime)

# Función para borrar los widgets de la pantalla de inicio
def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# Función para mostrar la fecha y hora en la pantalla de inicio
def show_datetime():
    clear_widgets()
    date_label.grid(row=0, column=0)
    time_label.grid(row=1, column=0)

# Crear una ventana Tkinter
root = tk.Tk()
root.title("Fecha, Hora y Menú")

# Etiqueta para la fecha
date_label = tk.Label(root, font=('calibri', 16))
date_label.grid(row=0, column=0)

# Etiqueta para la hora
time_label = tk.Label(root, font=('calibri', 16))
time_label.grid(row=1, column=0)

# Menú
menu = tk.Menu(root)
root.config(menu=menu)

option_menu = tk.Menu(menu)
menu.add_cascade(label="Opciones", menu=option_menu)
option_menu.add_command(label="Mostrar Fecha y Hora", command=show_datetime)
option_menu.add_separator()
option_menu.add_command(label="Opción 1")
option_menu.add_command(label="Opción 2")

# Iniciar la actualización de la fecha y hora
update_datetime()

root.mainloop()
