#Librerias
#-----------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from dataAnalisys import *

#Variables globales:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
filterDatagiven = False
#-----------------------------------------------------------------------------------------------------------------------------------------------------

root= Tk()
root.title("Hayek's app")
root.iconbitmap("icon.ico")

def toggle_listbox():
    global myLabel1, myLabel0, listboxAños
    if checkbox_var.get():
        myLabel0 = Label(root, text="Meses:")
        myLabel1 = Label(root, text="Años:")
        
        myLabel0.grid(row=2, column=2)
        myLabel1.grid(row=2, column=3)

        listboxMeses.grid(row=3, column=2)
        listboxAños.grid(row=3, column=3)

    else:
        listboxMeses.grid_forget()
        listboxAños.grid_forget()
        myLabel0.grid_forget()
        myLabel1.grid_forget()

    #TODO:
    #  selection_entry = tk.Entry(root, textvariable=selection_text, state="readonly")
    #  selection_entry.grid(row=3)


def checkButt():
    global checkbox_var, checkbox, listboxMeses, listboxAños, labelAño, labelMes, mesEntry, AñoEntry

    meses = dff.getMonthList()  # Lista de meses
    años = dff.getYearsList()   # Lista de años


    

    #listboxMeses.grid(row=1, column=1)



    #Inh
    if opcion1.get() == 1 and not(filterDatagiven):
        listboxMeses = Listbox(root, selectmode=SINGLE, selectbackground="blue")
        listboxAños = Listbox(root, selectmode=SINGLE, selectbackground="blue")

            # Agregar los meses al Listbox
        for mes in meses:
            listboxMeses.insert(END, mes)
        
        for año in años:
            listboxAños.insert(END, año)

        radio_button1.config(state=DISABLED)
        radio_button2.config(state=DISABLED)
        radio_button3.config(state=DISABLED)
        
        checkbox_var = IntVar()
        checkbox = Checkbutton(root, text="Mostrar Lista de Opciones", variable=checkbox_var, command=toggle_listbox)
        checkbox.grid(row=1, column=2)

        labelMes = Label(root, text="Mes seleccionado:")
        labelAño = Label(root, text="Año seleccionado:")

        labelMes.grid(row=4, column=0)
        labelAño.grid(row=4, column=1)

        mesEntry = Entry(root, textvariable="Buenas", state="readonly")
        mesEntry.grid(row=5, column=0)

        AñoEntry = Entry(root, textvariable="tardes", state="readonly")
        AñoEntry.grid(row=5, column=1)

    else:
        radio_button1.config(state=NORMAL)
        radio_button2.config(state=NORMAL)
        radio_button3.config(state=NORMAL)
        checkbox.grid_forget()
        labelMes.grid_forget()
        labelAño.grid_forget()
        mesEntry.grid_forget()
        AñoEntry.grid_forget()

        myLabel0.grid_forget()
        myLabel1.grid_forget()
        listboxMeses.grid_forget()
        listboxAños.grid_forget()


def showDataAnalisys():
    
    global opcion1, opcion2, radio_button1, radio_button2, radio_button3, botonFiltrado, dff
    opcion1 = IntVar()
    opcion2 = IntVar()

    dff=processData(archivo="Registro.csv")
    
    botonFiltrado = Checkbutton(root, text="Filtrar datos",   variable=opcion1, command=checkButt)
    botonFiltrado.grid(row=1, column=0, sticky='w')

    radio_button1 = Radiobutton(root, text="Gráficos", variable=opcion2, value=1, command=None)
    radio_button1.grid(row=6, column=0, sticky='w')

    radio_button2 = Radiobutton(root, text="Mostrar data-frame", variable=opcion2, value=2, command=None)
    radio_button2.grid(row=7, column=0, sticky='w')

    radio_button3 = Radiobutton(root, text="Observar éstadisticas", variable=opcion2, value=3, command=None)
    radio_button3.grid(row=8, column=0, sticky='w')




    #Boton de continuar:
    boton_conti = Button(root, text="Continuar", command=root.destroy,fg="green", bg="white")
    boton_conti.grid(row=9, column=1, sticky="w")

# Funciones para las opciones del menú
def opcion1():
    resultado.config(text="Analizando nuevo archivo")

def opcion2():
    resultado.config(text="Abriendo registro")
    showDataAnalisys()

# Función para salir de la aplicación
def salir():
    root.quit()


#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Crear un menú
menu_principal = Menu(root)
root.config(menu=menu_principal)

# Crear un menú desplegable "Opciones"
menu_opciones = Menu(menu_principal)
menu_principal.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Seleccionar archivo", command=opcion1)
menu_opciones.add_command(label="Abrir registro", command=opcion2)

# Agregar una opción para salir
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

# Etiqueta de resultado
resultado = Label(root, text="")
resultado.grid(row=0, column=0)

# Botón de salida:
boton_salir = Button(root, text="Salir", command=root.destroy,fg="red", bg="white")
boton_salir.grid(row=9, column=0, sticky="w")


root.mainloop()
"""
mostrarArchivos: Función para mostrar al usuario la cantidad de archivos
encontrados y sus respectivos nombres.

inputs:
    -archivos_en_carpeta: Lista con el nombre de archivos.
def mostrarArchivos(archivos_en_carpeta):
    root = Tk()
    nunArchivos = len(archivos_en_carpeta)
    displayArch = ""
    for archivo in archivos_en_carpeta:
        displayArch += ("\n-"+archivo)
    displayArch += "\n"
    

    #Labels:
    myLabeArch  = Label(root, text="Se han encontrado un total de "+str(nunArchivos)+" archivos",font=("Arial black",12))
    myLabeArch1 = Label(root, text=displayArch, anchor="e")

    myLabeArch.pack()
    myLabeArch1.pack()

    #Botones:
    continunar = Button(root, text="Continuar", font=("Verdana",11), command=lambda:cerar(root), padx=25, pady=5, bg="white")
    continunar.pack()

    root.mainloop()


cerar: Función para cerrar ventana. Si se procede con "continuar", enton-
ces la variable gobal "miDecision" se pone en True.

inputs:
    -miRoot: Root de la ventana.
def cerar(miRoot):
    miRoot.destroy()
    global miDecision
    miDecision = True
"""