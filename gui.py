#Librerias
#-----------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from dataAnalisys import *
from tkinter import ttk, messagebox
from pandasgui import show
#Variables globales:
#-----------------------------------------------------------------------------------------------------------------------------------------------------

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiempre", "Octubre", "Noviembre", "Diciembre"] 
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def obtener_seleccion():

    seleccion = opcion2.get()

    match seleccion:
        case 1:
            dataFrame.createGraph()
            dataFrame.boxGraph()
            dataFrame.piePlot()

        case 2:
            new_window = Toplevel()
            new_window.title("Estadísticas:")
            estadisticas=dataFrame.stadistics()
            results1 = Label(new_window, text="RESULTADOS OBTENIDOS", font=("Arial", 12, "bold"))
            resultado_label = Label(new_window, text=estadisticas, borderwidth=10, bg="White")
            results1.pack()
            resultado_label.pack()

        case 3:
            new_window = Toplevel()
            new_window.title("DataFrame:")
            
            """
            df_str = dataFrame.df.to_string()
            resultado_label = Label(new_window, text=df_str, borderwidth=10, bg="White")
            resultado_label.grid(sticky="w")
            resultado_label = Label(new_window, text=estadisticas, borderwidth=10, bg="White")
            """

            show(dataFrame.section, new_window)
        case _:
            pass

#Actualizar fechas a filtrar
def submitDates():
    if (añoEntry.cget("text")=="----") or (mesEntry.cget("text")=="----"):
        messagebox.showerror("Error", "Por favor asegurese de elegir una fecha")

    else:
        dataFrame.chooseSegment(mesXXX, año)
        radio_button1.config(state=NORMAL)
        radio_button2.config(state=NORMAL)
        radio_button3.config(state=NORMAL)
        boton_conti.config(state=NORMAL)

#Actualizar mes
def addFechasMes():
    global mesXXX
    mes1 = listboxMeses.get()
    if mes1 not in meses:
        messagebox.showerror("Error", "Por favor asegurese de elegir un mes valido")
    else:
        mesXXX = meses.index(mes1)+1
        mesEntry.config(text=str(mes1))

#Actualizar año
def addFechasAño():
    global año
    año = listboxAños.get()
    
    if año not in yrs:
        messagebox.showerror("Error", "Por favor asegurese de elegir un año valido")
    else:
        año=int(año)
        añoEntry.config(text=str(año))
        
#Elegir fechas:
def toggle_listbox():
    global myLabel1, myLabel0, buttonDates1, buttonDates2

    #Mostrar opciones de fechas
    if checkbox_var.get():
        myLabel0 = Label(root, text="Meses:")
        myLabel1 = Label(root, text="Años:")
        
        myLabel0.grid(row=2, column=2)
        myLabel1.grid(row=2, column=3)

        listboxMeses.grid(row=3, column=2)
        listboxAños.grid(row=3, column=3)

        buttonDates1 = Button(root, text="Seleccionar mes", bg="green", fg="White",  command=addFechasMes)
        buttonDates1.grid(row=4, column=2, padx=30)
        
        buttonDates2 = Button(root, text="Seleccionar año", bg="green", fg="White", command=addFechasAño)
        buttonDates2.grid(row=4, column=3, padx=30)

    else:
        listboxMeses.grid_forget()
        listboxAños.grid_forget()
        myLabel0.grid_forget()
        myLabel1.grid_forget()
        buttonDates1.grid_forget()
        buttonDates2.grid_forget()

        #casilla1.grid_forget()
        #casilla2.grid_forget()
        #casilla3.grid_forget()
        #casilla4.grid_forget()

#Filtrar datos check:
def checkButt():
    global checkbox_var, checkbox, listboxMeses, listboxAños, labelAño, labelMes, mesEntry, añoEntry, buttonDone, yrs
    
    yrs = dataFrame.getYearsList()   # Lista de años
    yrs = [str(elemento) for elemento in yrs]
    #Inh
    if opcion1.get() == 1 :

        listboxMeses = ttk.Combobox(root, values=meses)
        listboxAños =  ttk.Combobox(root,  values=yrs)


        radio_button1.config(state=DISABLED)
        radio_button2.config(state=DISABLED)
        radio_button3.config(state=DISABLED)
        boton_conti.config(state=DISABLED)

        #casilla1.config(state=DISABLED)
        #casilla2.config(state=DISABLED)
        #casilla3.config(state=DISABLED)
        #casilla4.config(state=DISABLED)

        checkbox_var = IntVar()
        checkbox = Checkbutton(root, text="Mostrar Lista de Opciones", variable=checkbox_var, command=toggle_listbox)
        checkbox.grid(row=1, column=2)

        labelMes = Label(root, text="Mes seleccionado:")
        labelAño = Label(root, text="Año seleccionado:")

        labelMes.grid(row=5, column=0)
        labelAño.grid(row=5, column=1)

        mesEntry = Label(root, text="----", bg="white", padx=30)
        mesEntry.grid(row=6, column=0)

        añoEntry = Label(root, text="----", bg="white", padx=30)
        añoEntry.grid(row=6, column=1)

        buttonDone = Button(root, text="Listo", relief=RAISED, font=("Helvetica", 12, "bold"), command=submitDates )
        buttonDone.grid(row=6, column=2)

    else:
        dataFrame.section = dataFrame.df

        radio_button1.config(state=NORMAL)
        radio_button2.config(state=NORMAL)
        radio_button3.config(state=NORMAL)
        boton_conti.config(state=NORMAL)

        #TODO:
        #casilla1.config(state=NORMAL)
        #casilla2.config(state=NORMAL)
        #casilla3.config(state=NORMAL)
        #casilla4.config(state=NORMAL)

        checkbox.grid_forget()
        labelMes.grid_forget()
        labelAño.grid_forget()
        mesEntry.grid_forget()
        añoEntry.grid_forget()

        buttonDone.grid_forget()
        myLabel0.grid_forget()
        myLabel1.grid_forget()
        listboxMeses.grid_forget()
        listboxAños.grid_forget()
        buttonDates1.grid_forget()
        buttonDates2.grid_forget()
        
        #TODO:
        #casilla1.grid_forget()
        #casilla2.grid_forget()
        #casilla3.grid_forget()
        #casilla4.grid_forget()


#Mostrar opciones de uso del analísis de datos:
def showDataAnalisys():
    
    global opcion1, opcion2, radio_button1, radio_button2, radio_button3, botonFiltrado, boton_conti
    
    
    opcion1 = IntVar()
    opcion2 = IntVar()

    
    botonFiltrado = Checkbutton(root, text="Filtrar datos",   variable=opcion1, command=checkButt)
    botonFiltrado.grid(row=1, column=0, sticky='w')

    radio_button1 = Radiobutton(root, text="Gráficos", variable=opcion2, value=1, command=None)
    radio_button1.grid(row=7, column=0, sticky='w')

    radio_button2 = Radiobutton(root, text="Observar estádisticas", variable=opcion2, value=2, command=None)
    radio_button2.grid(row=10, column=0, sticky='w')

    radio_button3 = Radiobutton(root, text="Analísis avanzado", variable=opcion2, value=3, command=None)
    radio_button3.grid(row=11, column=0, sticky='w')

    #Boton de continuar:
    boton_conti = Button(root, text="Continuar", command=obtener_seleccion,fg="green", bg="white")
    boton_conti.grid(row=12, column=1, sticky="w")

#TODO:
"""def graphOps():
    global casilla_var, casilla1, casilla2, casilla3, casilla4
    casilla_var = IntVar()

    casilla1 = Radiobutton(root, text="Ver evolución de gasto por fechas", variable=casilla_var , value=1)
    casilla1.grid(row=8, column=1, sticky='w')

    casilla2 = Radiobutton(root, text="Observar diagrama de caja", variable=casilla_var, value=2)
    casilla2.grid(row=9, column=1, sticky='w')

    
    casilla3 = Radiobutton(root, text="Porcentaje gastado por categoría", variable=casilla_var, value=3)
    casilla3.grid(row=8, column=2, sticky='w')

    casilla4 = Radiobutton(root, text="Todos", variable=casilla_var, value=4)
    casilla4.grid(row=9, column=2, sticky='w')

"""

# Funciones para las opciones del menú
def opcion1():
    resultado.config(text="Analizando nuevo archivo")

def opcion2():
    global dataFrame 
    resultado.config(text="Abriendo registro")
    dataFrame=processData(archivo="Registro.csv")
    showDataAnalisys()

# Función para salir de la aplicación
def rst():
    for widget in root.winfo_children():
        if widget !=menu_opciones and widget !=boton_rst:
            widget.grid_forget()


#%%
##-----------------------------------------------------------------------------------------------------------------------------------------------------
root= Tk()
root.title("Hayek's app")
root.iconbitmap("icon.ico")

# Crear un menú
menu_principal = Menu(root)
root.config(menu=menu_principal)

# Crear un menú desplegable "Opciones"
menu_opciones = Menu(menu_principal)
menu_principal.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Seleccionar archivo", command=opcion1)
menu_opciones.add_command(label="Abrir registro", command=opcion2)

# Agregar una opción para reiniciar el programa
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=root.destroy)

# Etiqueta de resultado
resultado = Label(root, text="")
resultado.grid(row=0, column=0)

# Botón de continuar:
boton_rst = Button(root, text="Reiniciar", command=rst,fg="green", bg="white")
boton_rst.grid(row=12, column=0, sticky="w")


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