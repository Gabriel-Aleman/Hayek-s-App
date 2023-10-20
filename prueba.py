import tkinter as tk

def move_object():
    canvas.move(obj, 5, 0)
    if canvas.coords(obj)[2] < window.winfo_width():
        window.after(50, move_object)

# Crear una ventana
window = tk.Tk()
window.title("Animación de Inicio")

# Crear un lienzo (canvas)
canvas = tk.Canvas(window, width=400, height=100, bg='white')
canvas.pack()

# Crear un objeto (por ejemplo, un rectángulo)
obj = canvas.create_rectangle(0, 30, 50, 70, fill='blue')

# Iniciar la animación
move_object()

window.mainloop()
