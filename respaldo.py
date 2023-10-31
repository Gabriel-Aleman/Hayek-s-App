from tkinter import *
import os

from tkinter import ttk, messagebox, filedialog
from tkinter import filedialog
from fileManagement import *
from dataAnalisys import *

categoria   = ["Transporte", "Comida", "Entretenimiento", "Impuestos", "Servicios públicos", "Otros"]

def siguiente_dato(conceptos, length):
    global miIndice
    # Obtener el dato ingresado
    dato = combo_Cat.get()

    # Agregar el dato a la lista de datos
    datos.append(dato)

    # Aumentar el índice para seguir con el siguiente dato
    miIndice += 1


    if miIndice < length:
        "+str(miIndice+1)+"
        # Cambiar la etiqueta para pedir el siguiente dato
        labelConcepto.config(text=conceptos[miIndice])
        labelX.config( text="Concepto "+str(miIndice+1)+":")
    else:
        # Si se ingresaron los 5 datos, mostrar los datos y cerrar la ventana
        df1.addCategories(datos)
        buttonSave.config(state="normal")
        buttonProcesar.config(state="normal")
        messagebox.showinfo("Exito", "Se añadieron las categorías existosamente.")
        print(df1.df)
        nueva_ventana.destroy()


def askCategories():
    global datos, combo_Cat, labelConcepto, nueva_ventana, miIndice, labelX
    miIndice = 0
    datos = []  # Lista para almacenar los datos
    
    nueva_ventana = Toplevel(root)
    nueva_ventana.title("Ingresando categorías")

    conceptos = df1.df["Concepto"].to_list()

    labelX =Label(nueva_ventana, text="Concepto 1:")
    labelX.grid(row=0, column=0, sticky="e")

    labelConcepto =Label(nueva_ventana, text=conceptos[miIndice])
    labelConcepto.grid(row=0, column=1)

    labelY =Label(nueva_ventana, text="Cateogría: ")
    labelY.grid(row=1, column=0, sticky="e")

    addCat = Button(nueva_ventana, text="Siguiente", command=lambda : siguiente_dato(conceptos, len(conceptos)))
    addCat.grid(row=2, column=0, sticky="e")


    combo_Cat = ttk.Combobox(nueva_ventana, values=categoria)
    combo_Cat.grid(row=1, column=1)


def formatData():
    global df1

    tipoX =tipo_combobox.get()

    try:
        df1 = createDataFrame(archivo,  tipoX)
        messagebox.showinfo("Exito", "Sus datos fueron procesados correctamente.")
    except:
        messagebox.showerror("Error", "Asegurese de que el archivo y el tipo de banco especificados estén bien")
    else:
        buttonCat    = Button(root, text="Añadir categorias", command = askCategories, fg="green", bg="white", font=("Bold",9))
        buttonCat.grid(row=6, column=1, sticky="w", padx=5, pady=10)
        
        df1= processData(df1, tipoX)
        print(df1.df)


#-----------------------------------------------------------------------------------------------------------------------------------------
# Función que se ejecuta cuando se cambia el estado del CheckBox
def toggle_listbox_state():
    if checkbox_var.get():
        archivosEnCarpeta.grid(row=2, column=0, sticky="w") # Deshabilitar el ListBox
    else:
        archivosEnCarpeta.grid_forget() # Deshabilitar el ListBox


def checkExtent(archivo1, extension1):
    global archivo, extension
    ruta_labelRes.config(text=f"{archivo1}")
    exte_labelRes.config(text=f"{extension1}")
    tipo_label.grid(row=5, column=0, sticky="w")
    submitButton.grid(row=6, column=0, sticky="w")
    tipo_combobox.grid(row=5, column=1, sticky="w")

    extension= extension1
    archivo  = archivo1
    

def seleccionarDeCarpeta(event):
    seleccion = archivosEnCarpeta.curselection()

    if seleccion:
        indice = seleccion[0]
        archivo1 = archivosEnCarpeta.get(indice)
        extension1 = archivo1[-4:].lower()
        checkExtent(archivo1, extension1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Función para abrir un archivo
def abrir_archivo():
    try:
        checkbox.grid_forget()
        archivosEnCarpeta.grid_forget()
    except:
        pass
    
    archivo1 = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf"), ("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")])

    if archivo1:
        extension1 = os.path.splitext(archivo1)[1]
        checkExtent(archivo1, extension1)

def carpeta_archivo():
    global checkbox_var, checkbox
    # Crear una variable Tkinter para el estado del CheckBox
    checkbox_var = BooleanVar()
    checkbox = Checkbutton(root, text="Ver archivos en carpeta predeterminada", variable=checkbox_var, command=toggle_listbox_state)
    checkbox.grid(row=1, column=0, sticky="w")
    
    archivosEnCarpeta.grid(row=2, column=0, sticky="w") # Deshabilitar el ListBox

    if(len(misArchivos)>0):
        toggle_listbox_state()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def guardarEnCSV():
    respuesta = messagebox.askyesno("Pregunta", "¿Está seguro que quiere añadir estos datos al registro?")
    if respuesta:  # Si el usuario elige "Sí"
        messagebox.showinfo("Exito", "Se añadieron guardaron los datos existosamente.")
        df1.guardar_csv()

    

def abrirArchivo():
    global archivosEnCarpeta, ruta_labelRes, exte_labelRes, misArchivos, tipo_combobox, submitButton, tipo_label, buttonSave, buttonProcesar


    fuente_personalizada = ("Bahnschrift", 9)

    #Botones de las opciones generales
    buttonCarpeta = Button(root, text="Abrir manualmente archivo",   command   = abrir_archivo, bg="green", fg="white"  , relief="solid", font=("Bold",9))
    buttonCarpeta.grid(row=0, column=1, sticky="w", pady=10, padx=8)

    buttonFile    = Button(root, text="Revisar carpeta predertimanada", command = carpeta_archivo, bg="green", fg="white",relief="solid", font=("Bold",9))
    buttonFile.grid(row=0, column=0, sticky="w",    pady=10, padx=8)

    #Botones para continuar:

    #ListBox para los archivos disponibles en la carpeta predeterminada
    archivosEnCarpeta = Listbox(root, width=55)
    misArchivos         = encontrarArchivos(ruta_carpeta)

    for archivox in misArchivos:
        archivosEnCarpeta.insert(END, archivox)
        archivosEnCarpeta.bind("<<ListboxSelect>>", seleccionarDeCarpeta)

    fuente_personalizada = ("Bahnschrift", 9)
    
    # Label para mostrar la ruta del archivo
    ruta_label = Label(root, text="•Ruta del archivo seleccionado: ", font=fuente_personalizada)
    ruta_label.grid(row=3, column=0, sticky="w")

    exte_label = Label(root, text="•Extensión del archivo seleccionado: ", font=fuente_personalizada)
    exte_label.grid(row=4, column=0, sticky="w")


    ruta_labelRes = Label(root, text="", fg="green")
    ruta_labelRes.grid(row=3, column=1, sticky="w")

    exte_labelRes = Label(root, text="", fg="green")
    exte_labelRes.grid(row=4, column=1, sticky="w")

    #Tipo de banco:
    tipo_label = Label(root, text="•Tipo de banco: ", font=fuente_personalizada)
    tipo_combobox = ttk.Combobox(root, values=bancos)

    submitButton = Button(root, text="Procesar datos", command=formatData, bg="white", fg="green")
    
    #Opciones a posteriorí:
    buttonRst    = Button(root, text="Reinciar", command = None, fg="green", bg="white", font=("Bold",9))
    buttonRst.grid(row=7, column=0, sticky="w", pady=10)

    buttonSave    = Button(root, text="Guardar datos en el registro", command = guardarEnCSV, fg="green", bg="white", font=("Bold",9))
    buttonSave.grid(row=7, column=1, sticky="w",  pady=10)

    buttonProcesar    = Button(root, text="Analizar estos datos", command = None, fg="green", bg="white", font=("Bold",9))
    buttonProcesar.grid(row=7, column=2, sticky="w",  pady=10)

    buttonSave.config(state="disabled")
    buttonProcesar.config(state="disabled")



    

    
# Configuración de la root

root = Tk()
root.title("Seleccionar Opción")
abrirArchivo()


root.mainloop()