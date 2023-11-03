import tkinter as tk
from tkinter import ttk

# Función para llenar la tabla con datos
def fill_table():
    # Supongamos que tienes datos en forma de lista de listas
    data = [
        ["1", "John", "Doe"],
        ["2", "Jane", "Smith"],
        ["3", "Alice", "Johnson"]
        # Puedes agregar más datos aquí si es necesario
    ]

    # Eliminar datos existentes de la tabla (si los hay)
    for row in tree.get_children():
        tree.delete(row)

    # Insertar los datos en la tabla
    for record in data:
        tree.insert("", "end", values=record)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de tabla en Tkinter")

# Crear un contenedor para la tabla
tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10)

# Crear la tabla
tree = ttk.Treeview(tree_frame, columns=("ID", "Nombre", "Apellido"), show="headings")
tree.pack()

# Configurar las columnas
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")

# Establecer el ancho de las columnas
tree.column("ID", width=50)
tree.column("Nombre", width=100)
tree.column("Apellido", width=100)

# Botón para llenar la tabla con datos
fill_button = ttk.Button(root, text="Llenar Tabla", command=fill_table)
fill_button.pack()

# Mostrar la ventana
root.mainloop()
