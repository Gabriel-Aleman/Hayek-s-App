#Librerias
#-----------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
from dataAnalisys import *

from tkinter import ttk, messagebox
from pandastable import Table, TableModel
from PIL import Image, ImageTk
#Variables globales:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def actualizar_gif(frame):
    try:
        # Carga el siguiente frame del GIF
        image.seek(frame)
        foto = ImageTk.PhotoImage(image)

        # Actualiza la etiqueta con el nuevo frame
        coin.configure(image=foto)
        coin.image = foto

        # Establece un temporizador para el siguiente frame
        root.after(100, actualizar_gif, frame + 1)
    except EOFError:
        # Cuando llegamos al final del GIF, reiniciamos desde el principio
        actualizar_gif(0)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiempre", "Octubre", "Noviembre", "Diciembre"]
categoria = ["Transporte", "Comida", "Entretenimiento", "Impuestos", "Servicios públicos", "Otros"]
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def obtener_seleccion():
    seleccion = elegirFuncion.get()

    if seleccion == 0:     #Revisar que el usuario halla elegido una opción
        messagebox.showerror("Error", "Debe seleccionar una opción.")
    else:
        #Elegir la opción
        match seleccion:
            case 1: #Gráficos
                dataFrame.createGraph()
                dataFrame.boxGraph()
                dataFrame.piePlot()

            case 2: #Estadísticas
                new_window = Toplevel()
                new_window.title("Estadísticas:")
                estadisticas=dataFrame.stadistics()
                results1 = Label(new_window, text="RESULTADOS OBTENIDOS", font=("Arial", 12, "bold"))
                resultado_label = Label(new_window, text=estadisticas, borderwidth=10, bg="White")
                results1.pack()
                resultado_label.pack()

            case 3: #Ver data-Frame
                df=dataFrame.section
                new_window = Toplevel()
                new_window.title("DataFrame:")

                # Crear un modelo de datos para PandasTable
                modelo = TableModel(dataframe=df, columns=4)

                # Crear una tabla con PandasTable en la nueva ventana
                tabla = Table(new_window, model=modelo, showtoolbar=True)
                tabla.show()


            case _:
                pass

#Actualizar fechas a filtrar
def submitDates():
    addFechasMes()
    addFechasAño()

    if (añoDone and mesDone):
        dataFrame.chooseSegment(mes, año)
        radio_buttonGraficos.config(state=NORMAL)
        radio_buttonEstadistics.config(state=NORMAL)
        radio_buttonDF.config(state=NORMAL)
        boton_conti.config(state=NORMAL)

        """        
        botonPlot.config(state=NORMAL)
        botonPie.config(state=NORMAL)
        botonBox.config(state=NORMAL)
        botonAll.config(state=NORMAL)
        """

    else:
        radio_buttonGraficos.config(state=DISABLED)
        radio_buttonEstadistics.config(state=DISABLED)
        radio_buttonDF.config(state=DISABLED)
        boton_conti.config(state=DISABLED)

        """
        botonPlot.config(state=DISABLED)
        botonPie.config(state=DISABLED)
        botonBox.config(state=DISABLED)
        botonAll.config(state=DISABLED)
        """


#Actualizar mes
def addFechasMes():
    global mes, mesDone #TODO; mesDone
    mes = listboxMeses.get()

    try:    #Verificar si es un número:
        mes = int(mes)  # Intenta convertir la cadena en un número de coma flotante    
    
    except ValueError:  #No es un número:
        mesesChec = [miMes.lower() for miMes in meses]
        if  mes.lower() not in mesesChec:
            mesDone = False
        else:
            mes = mesesChec.index(mes.lower())+1
            mesDone = True
    else:               #Sí es un número
        if mes<=12 and mes>=1:
            mesDone = True
        else:
            mesDone =False
    
    if(mesDone):
        if widget_exists(mesEntry):
            mesEntry.config(text=meses[mes-1])
    else:
        messagebox.showerror("Error", "Por favor asegurese de elegir un mes valido")



#Actualizar año
def addFechasAño():
    global año, añoDone
    año = listboxAños.get()
    
    try:
        año=int(año)
    except ValueError:  #El año no es un número
        añoDone = False
    else:               #El año sí es un número
        if año in yrs:
            añoDone = True
        else:
            añoDone = False

    if(añoDone):
        if widget_exists(añoEntry):
            añoEntry.config(text=str(año))
    else:
        messagebox.showerror("Error", "Por favor asegurese de elegir un año valido")
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


#Filtrar datos check:
def checkButt():
    global checkbox_var, checkbox, labelAño, labelMes, mesEntry, añoEntry, buttonDone, yrs, listboxMeses, listboxAños
    
    yrs = dataFrame.getYearsList()   # Lista de años

    #Inh
    if habilitarFiltrado.get() == 1 :

        listboxMeses = ttk.Combobox(root, values=meses)
        listboxAños =  ttk.Combobox(root,  values=yrs)


        radio_buttonGraficos.config(state=DISABLED)
        radio_buttonEstadistics.config(state=DISABLED)
        radio_buttonDF.config(state=DISABLED)
        boton_conti.config(state=DISABLED)

        """
        if(elegirFuncion.get()==1):
            botonPlot.config(state=DISABLED)
            botonPie.config(state=DISABLED)
            botonBox.config(state=DISABLED)
            botonAll.config(state=DISABLED)
        """


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

        radio_buttonGraficos.config(state=NORMAL)
        radio_buttonEstadistics.config(state=NORMAL)
        radio_buttonDF.config(state=NORMAL)
        boton_conti.config(state=NORMAL)
        """

        if(elegirFuncion.get()==1):
            botonPlot.config(state=NORMAL)
            botonPie.config(state=NORMAL)
            botonBox.config(state=NORMAL)
            botonAll.config(state=NORMAL)
        """

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
        


#Mostrar opciones de uso del analísis de datos:
def showDataAnalisys():
    global habilitarFiltrado, elegirFuncion, habilitarGraf, radio_buttonGraficos, radio_buttonEstadistics, radio_buttonDF, botonFiltrado, boton_conti, botonGraf
    habilitarFiltrado = IntVar()
    elegirFuncion = IntVar()
    habilitarGraf = IntVar()

    botonGraf = Checkbutton(root, text="Escoger gráfico",   variable=habilitarGraf)

    
    botonFiltrado = Checkbutton(root, text="Filtrar datos",   variable=habilitarFiltrado, command=checkButt)
    botonFiltrado.grid(row=1, column=0, sticky='w')

    radio_buttonGraficos = Radiobutton(root, text="Gráficos", variable=elegirFuncion, value=1, command=chekOps)
    radio_buttonGraficos.grid(row=7, column=0, sticky='w')

    radio_buttonEstadistics = Radiobutton(root, text="Observar estádisticas", variable=elegirFuncion, value=2, command=botonGraf.grid_forget)
    radio_buttonEstadistics.grid(row=10, column=0, sticky='w')

    radio_buttonDF = Radiobutton(root, text="Ver data-frame", variable=elegirFuncion, value=3, command=botonGraf.grid_forget)
    radio_buttonDF.grid(row=11, column=0, sticky='w')

    #Boton de continuar:
    boton_conti = Button(root, text="Continuar", command=obtener_seleccion,fg="green", bg="white")
    boton_conti.grid(row=12, column=1, sticky="w")

            

def chekOps():
    global botonPlot, botonAll, botonBox, botonPie, tipoGrafico

    tipoGrafico = StringVar()

    botonGraf.grid(row=7, column=2, sticky="W")
    botonPlot   = Radiobutton(root, text="Monto en función del tiempo", variable=tipoGrafico, value="plt", command=None)
    botonPie    = Radiobutton(root, text="Gasto por categoría",         variable=tipoGrafico, value="cat", command=None)
    botonBox    = Radiobutton(root, text="Diagrama de caja",            variable=tipoGrafico, value="box", command=None)
    botonAll    = Radiobutton(root, text="todos",                       variable=tipoGrafico, value="all", command=None)

    if habilitarGraf.get()==1:
        print("HOLA")

        botonPlot.grid(row=8, column=0, sticky="W")
        botonPie.grid(row=8, column=1, sticky="W")

        botonBox.grid(row=9, column=0, sticky="W")
        botonAll.grid(row=9, column=1, sticky="W")
    else:
        print("Adios")

        botonPlot.grid_forget()
        botonPie.grid_forget()
        botonBox.grid_forget()
        botonAll.grid_forget()


def forget():
    botonPlot.grid_forget()
    botonPie.grid_forget()
    botonBox.grid_forget()
    botonAll.grid_forget()
    
def guardar_datos():
    miMes = str(meses.index(listboxMeses.get())+1)
    miDia = listboxDia.get()

    if int(miMes)<10:
        miMes="0"+miMes

    if int(miDia)<10:
        miDia="0"+miDia


    fecha = f"{listboxAños.get()}-{miMes}-{listboxDia.get()}"
    monto = entry_monto.get()
    concepto = entry_concepto.get()
    categoria = listboxCategoria.get()
    
    miSTR= fecha+","+concepto+","+monto+","+categoria+"\n"
    
    #Guardar en archivo
    with open("Registro.csv", 'a') as archivo:
        archivo.write(miSTR)

# Funciones para las opciones del menú
def habilitarFiltrado():
    rst()
    coin.grid_forget()
    resultado.config(text="Analizando nuevo archivo")

def elegirFuncion():
    global dataFrame
    rst()
    coin.grid_forget()
    resultado.config(text="Abriendo registro")
    dataFrame=processData(archivo="Registro.csv")
    showDataAnalisys()

def añadirDato():
    global  entry_monto, entry_concepto, guardado, listboxMeses, listboxDia, listboxAños, listboxCategoria
    rst()
    coin.grid_forget()

    # Crear etiquetas y campos de entrada para cada dato
    label_mes = Label(root, text="Mes:")
    listboxMeses = ttk.Combobox(root, values=meses)


    label_dia = Label(root, text="Día:")
    listboxDia = ttk.Combobox(root, values=list(range(1, 31)))

    label_anio = Label(root, text="Año:")
    listboxAños =  ttk.Combobox(root,  values=list(range(2000, 2023)))

    label_categoria = Label(root, text="Categoría:")
    listboxCategoria = ttk.Combobox(root, values=categoria)

    label_monto = Label(root, text="Monto:")
    entry_monto = Entry(root)

    label_concepto = Label(root, text="Concepto:")
    entry_concepto = Entry(root)


    # Botón para guardar los datos
    boton_guardar = Button(root, text="Guardar", command=guardar_datos)

    # Etiqueta para mostrar los datos ingresados
    guardado = Label(root, text="")

    # Colocar etiquetas y campos de entrada en la ventana
    label_mes.grid(row=0, column=0, sticky="w")
    listboxMeses.grid(row=0, column=1)

    label_dia.grid(row=1, column=0, sticky="w")
    listboxDia.grid(row=1, column=1)

    label_anio.grid(row=2, column=0, sticky="w")
    listboxAños.grid(row=2, column=1)

    label_categoria.grid(row=3, column=0, sticky="w")
    listboxCategoria.grid(row=3, column=1)

    label_monto.grid(row=4, column=0, sticky="w")
    entry_monto.grid(row=4, column=1)

    label_concepto.grid(row=5, column=0, sticky="w")
    entry_concepto.grid(row=5, column=1)

    boton_guardar.grid(row=12, column=0, columnspan=2)
    guardado.grid(row=18, column=0)


# Función para salir de la aplicación
def rst():
    for widget in root.winfo_children():
        if widget !=menu_opciones and widget !=boton_rst:
            widget.grid_forget()

    coin.grid(row=0,column=0, padx=100, pady=100)


def widget_exists(widget):
    try:
        widget.winfo_exists()
        return True
    except:
        return False


#%% MAIN:
##-----------------------------------------------------------------------------------------------------------------------------------------------------

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