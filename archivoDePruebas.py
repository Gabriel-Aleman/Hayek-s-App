import tkinter as tk

def opcion_seleccionada():
    seleccion = var.get()
    if seleccion == 1:
        print("Opción A seleccionada")
    elif seleccion == 2:
        print("Opción B seleccionada")
    else:
        print("Opción C seleccionada")

root = tk.Tk()
root.title("Personalización de Radio Buttons")

# Variables de control
var = tk.IntVar()
var.set(1)

# Estilos para los Radio Buttons
estilo_radio = {
    "indicatoron": 0  # Eliminar el círculo alrededor del botón
}

opcion_a = tk.Radiobutton(root, text="Opción A", variable=var, value=1, command=opcion_seleccionada, **estilo_radio)
opcion_a.pack()

opcion_b = tk.Radiobutton(root, text="Opción B", variable=var, value=2, command=opcion_seleccionada, **estilo_radio)
opcion_b.pack()

opcion_c = tk.Radiobutton(root, text="Opción C", variable=var, value=3, command=opcion_seleccionada, **estilo_radio)
opcion_c.pack()

root.mainloop()
