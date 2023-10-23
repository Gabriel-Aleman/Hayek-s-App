from gui import *
root= Tk()
root.title("Hayek's app")
root.iconbitmap("icon.ico")



#root.wm_attributes('-zoomed', False)  # Deshabilita el botón de maximizar
#root.wm_attributes('-topmost', True)   # Mantiene la ventana en la parte superior
# Crear un menú
menu_principal = Menu(root)


root.config(menu=menu_principal)

# Crear un menú desplegable "Opciones"
menu_opciones = Menu(menu_principal)
menu_principal.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Seleccionar archivo", command=habilitarFiltrado)
menu_opciones.add_command(label="Abrir registro", command=elegirFuncion)
menu_opciones.add_command(label="Añadir dato al registro manual", command=añadirDato)


# Agregar una opción para reiniciar el programa
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=root.destroy)

# Etiqueta de resultado
resultado = Label(root, text="")
resultado.grid(row=0, column=0)

# Botón de continuar:
boton_rst = Button(root, text="Reiniciar", command=rst,fg="green", bg="white")
boton_rst.grid(row=12, column=0, sticky="w")

image = Image.open("coin.gif")
foto = ImageTk.PhotoImage(image)
# Crear un widget de etiqueta para mostrar la imagen
coin = Label(root, image=foto)
coin.grid(row=0,column=0, padx=100, pady=100)
# Inicia el ciclo de actualización del GIF
actualizar_gif(0)

root.mainloop()