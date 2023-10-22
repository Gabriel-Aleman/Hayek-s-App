import tkinter as tk

def on_cell_edit(row, col, value):
    # Esta función maneja la edición de celdas
    data[row][col] = value

def update_table():
    # Actualiza la tabla en función de los datos
    for i in range(rows):
        for j in range(columns):
            entry = entries[i][j]
            entry.delete(0, tk.END)
            entry.insert(0, data[i][j])

root = tk.Tk()
root.title("Tabla en tkinter")

# Datos de ejemplo
data = [["Celda 00", "Celda 01", "Celda 02"],
        ["Celda 10", "Celda 11", "Celda 12"],
        ["Celda 20", "Celda 21", "Celda 22"]]
rows = len(data)
columns = len(data[0])

# Crear una lista de listas para almacenar las celdas editables
entries = []
for i in range(rows):
    row_entries = []
    for j in range(columns):
        entry = tk.Entry(root, width=15)
        entry.grid(row=i, column=j)
        entry.insert(0, data[i][j])
        entry.bind("<FocusOut>", lambda event, row=i, col=j, entry=entry: on_cell_edit(row, col, entry.get()))
        row_entries.append(entry)
    entries.append(row_entries)

# Crear un botón para actualizar la tabla
update_button = tk.Button(root, text="Actualizar Tabla", command=update_table)
update_button.grid(row=rows, columnspan=columns)

root.mainloop()
