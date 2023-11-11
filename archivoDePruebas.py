"""import tkinter as tk
from tkinter import ttk

def mostrar_contenido(event):
    current_tab = notebook.index(notebook.select())
    if current_tab == 0:
        label_texto.config(text="Contenido de la Pestaña 1")
    elif current_tab == 1:
        label_texto.config(text="Contenido de la Pestaña 2")
    elif current_tab == 2:
        label_texto.config(text="Contenido de la Pestaña 3")

# Crear la ventana principal
root = tk.Tk()
root.title("Notebook con Tkinter")
root.geometry("400x300")

# Crear el notebook (pestañas)
notebook = ttk.Notebook(root)

# Pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Agregar pestañas al notebook
notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')
notebook.add(tab3, text='Pestaña 3')

notebook.pack(expand=1, fill="both")

# Contenido de las pestañas
label_texto = tk.Label(root, text="", width=30)
label_texto.pack()

# Manejar evento al cambiar de pestaña
notebook.bind("<<NotebookTabChanged>>", mostrar_contenido)

root.mainloop()
"""
from tkinter import *

from tkinter import *



def main():
    root = Tk()
    root.title("Tabla en Tkinter")

    # Datos de ejemplo para la tabla (2 columnas, 7 filas)
    datos = [
        ["Parametro", "Valor"],
        ["Juan", 25],
        ["María", 30],
        ["Carlos", 22],
        ["Ana", 28],
        ["Luis", 35],
        ["Laura", 29],
        ["Pedro", 31]
    ]

    # Crear la tabla utilizando la función
    crear_tabla(root, datos)

    root.mainloop()

if __name__ == "__main__":
    main()
