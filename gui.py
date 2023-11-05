from edit import *
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#%%LEEER ARCHIVO:   
#-----------------------------------------------------------------------------------------------------------------------------------------------------

def proccessFile(myDf):
    chooseFunc(myDf)


def askCategories():
    global datos, combo_Cat, labelConcepto, nueva_ventana, labelX, misNuevosElementos, indiceCategoras
    useSavedConcepts = False
    mi_diccionario= readSavedConcepts() #Categorías guardadas


    conceptos = df1.df["Concepto"].to_list()
    datos =  [None for _ in conceptos]
    
    misIndices = []             #Elementos a guardar
    indiceCategoras = 0

    if len(mi_diccionario) != 0:
        useSavedConcepts = messagebox.askyesno("Pregunta", "¿Desea asignar aútomaticamente las categorías a concetos ya guardados?")

    nueva_ventana = Toplevel(root)
    nueva_ventana.resizable(False, False)

    nueva_ventana.iconbitmap("iconos/lista.ico")

    
    nueva_ventana.title("Ingresando categorías")

    if useSavedConcepts:
        for i in range(len(conceptos)):
            if conceptos[i] in mi_diccionario:
                datos[i] = mi_diccionario[conceptos[i]]
            else:
                misIndices.append(i)    #Elemento donde hay un None
    else:
        misIndices = list(range(len(conceptos)))

    misNuevosElementos = [None for _ in misIndices]     #Valores  a guardar

    
    labelX =Label(nueva_ventana, text="Concepto 1:")
    labelX.grid(row=0, column=0, sticky="e")

    labelConcepto =Label(nueva_ventana, text=conceptos[misIndices[0]])
    labelConcepto.grid(row=0, column=1)

    labelY =Label(nueva_ventana, text="Cateogría: ")
    labelY.grid(row=1, column=0, sticky="e")

    addCat = Button(nueva_ventana, text="Siguiente", command=lambda : siguiente_dato(conceptos, len(misIndices), misIndices), bg="green", fg="white", width=20)
    addCat.grid(row=2, column=1, pady=5)

    back = Button(nueva_ventana, text="Anterior", command=lambda: datoAnterior(conceptos, misIndices), bg="green", fg="white", width=20)
    back.grid(row=2, column=0, pady=5, padx=5)

    combo_Cat = ttk.Combobox(nueva_ventana, values=categoria)
    combo_Cat.grid(row=1, column=1)

def siguiente_dato(conceptos, length, misIndices):
    global indiceCategoras
    # Obtener el dato ingresado
    dato = combo_Cat.get()

    # Agregar el dato a la lista de datos
    misNuevosElementos[indiceCategoras]=dato

    # Aumentar el índice para seguir con el siguiente dato
    indiceCategoras = indiceCategoras+1


    if indiceCategoras < length:
        # Cambiar la etiqueta para pedir el siguiente dato
        labelConcepto.config(text=conceptos[misIndices[indiceCategoras]])
        labelX.config( text="Concepto "+str(indiceCategoras+1)+":")
    else:
        for i in range(len(misIndices)):
            datos[misIndices[i]]=misNuevosElementos[i]
            
        # Si se ingresaron los 5 datos, mostrar los datos y cerrar la ventana
        df1.addCategories(datos)
        buttonSave.config(state="normal")
        buttonProcesar.config(state="normal")
        messagebox.showinfo("Exito", "Se añadieron las categorías existosamente.")
        print(df1.df)
        nueva_ventana.destroy()

def datoAnterior(conceptos, misIndices):
    global indiceCategoras

    if indiceCategoras>=1:

        # Aumentar el índice para seguir con el siguiente dato
        indiceCategoras = indiceCategoras-1
        
        # Cambiar la etiqueta para pedir el siguiente dato
        labelConcepto.config(text=conceptos[misIndices[indiceCategoras]])
        labelX.config( text="Concepto "+str(indiceCategoras+1)+":")

    else: 
        pass

def formatData():
    global df1

    tipoX =tipo_combobox.get()
    
    print(archivo, tipoX) 
    try:
        df1 = createDataFrame(archivo,  tipoX)
        messagebox.showinfo("Exito", "Sus datos fueron procesados correctamente.")
    except:
        messagebox.showerror("Error", "Asegurese de que el archivo y el tipo de banco especificados estén bien")
        buttonSave.config(state="disabled")
        buttonProcesar.config(state="disabled")
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
        archivo1 = "archivos/"+archivosEnCarpeta.get(indice)
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

#Función para abrir carpeta predeterminada:
def carpeta_archivo():
    global checkbox_var, checkbox
    # Crear una variable Tkinter para el estado del CheckBox
    checkbox_var = BooleanVar()
    checkbox = Checkbutton(root, text="Ver archivos en carpeta predeterminada", variable=checkbox_var, command=toggle_listbox_state)
    checkbox.grid(row=1, column=0, sticky="w")
    
    archivosEnCarpeta.grid(row=2, column=0, sticky="w") # Deshabilitar el ListBox

    if(len(misArchivos)>0):
        toggle_listbox_state()

#Guardar datos del archivo en un CSV
def guardarEnCSV():
    respuesta = messagebox.askyesno("Pregunta", "¿Está seguro que quiere añadir estos datos al registro?")
    if respuesta:  # Si el usuario elige "Sí"
        messagebox.showinfo("Exito", "Se añadieron guardaron los datos existosamente.")
        df1.guardar_csv()

    
#Inicio de la opción de archivos:
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
    buttonSave    = Button(root, text="Guardar datos en el registro", command = guardarEnCSV, fg="green", bg="white", font=("Bold",9))
    buttonSave.grid(row=12, column=1, sticky="w",  pady=10)

    buttonProcesar    = Button(root, text="Analizar estos datos", command = lambda: proccessFile(df1), fg="green", bg="white", font=("Bold",9))
    buttonProcesar.grid(row=12, column=2, sticky="w",  pady=10)

    buttonSave.config(state="disabled")
    buttonProcesar.config(state="disabled")

#%%ABRIR REGISTRO
#En base a la opción elegida por el usuario mostrar los resultados
def obtener_seleccion():
    seleccion = elegirFuncion.get()

    if seleccion == 0:     #Revisar que el usuario halla elegido una opción
        messagebox.showerror("Error", "Debe seleccionar una opción.")

    elif dataFrame.section.empty:
        messagebox.showerror("Error", "Los rangos seleccionados no tienen información.")
    
    else:
        if habilitarFiltrado.get(): #Revisar si se filtraron por fechas
            appendFechas= f" (Mes: {mes} - Año: {año})"
            titGraph = dataFrame.createGraph.__defaults__[0]+appendFechas
            titCat = dataFrame.categPlot.__defaults__[0]+appendFechas
            titBox = dataFrame.boxGraph.__defaults__[0]+appendFechas
            titHist = dataFrame.hist.__defaults__[0]+appendFechas

        else:
            titGraph = dataFrame.createGraph.__defaults__[0]
            titCat = dataFrame.categPlot.__defaults__[0]
            titBox = dataFrame.boxGraph.__defaults__[0]
            titHist = dataFrame.hist.__defaults__[0]


        #Elegir la opción
        match seleccion:
            case 1: #Gráficos
                opc=tipoGrafico.get()
                if opc==0:
                    messagebox.showerror("Error", "Por favor asegurese de elegir un tipo de gráfico")
                else:
                    match opc:
                        case 1:
                            dataFrame.createGraph(miTitulo=titGraph)
                        case 2:
                            dataFrame.categPlot(miTitulo=titCat)
                        case 3:
                            dataFrame.boxGraph(miTitulo=titBox)
                        case 4:
                            dataFrame.categPlot(miTitulo=titCat, pie=False)
                        case 5:
                            dataFrame.hist(miTitulo=titHist, defBins=bins)
                        case 6:
                            dataFrame.createGraph(miTitulo=titGraph)
                            dataFrame.categPlot(miTitulo=titCat)
                            dataFrame.categPlot(miTitulo=titCat,pie=False)
                            dataFrame.boxGraph(miTitulo=titBox)
                            dataFrame.hist(miTitulo=titHist, defBins=bins)


            case 2: #Estadísticas
                new_window = Toplevel()
                new_window.resizable(False, False)

                new_window.iconbitmap("iconos/icon.ico")

                new_window.title("Estadísticas:")
                estadisticas=dataFrame.stadistics()
                results1 = Label(new_window, text="RESULTADOS OBTENIDOS", font=("Arial", 12, "bold"), fg="green")
                resultado_label = Label(new_window, text=estadisticas, borderwidth=5, bg="White", justify='left', wraplength=200, font=("Helvetica", 13))
                results1.grid(row=0, column=0, sticky="w")
                resultado_label.grid(row=1,column=0)

            case 3: #Ver data-Frame
                df=dataFrame.section
                new_window = Toplevel()
                new_window.resizable(False, False)
                new_window.iconbitmap("iconos/tabla.ico")
                new_window.title("DataFrame:")

                # Crear un modelo de datos para PandasTable
                modelo = TableModel(dataframe=df, columns=4)

                # Crear una tabla con PandasTable en la nueva ventana
                tabla = Table(new_window, model=modelo, showtoolbar=True)
                tabla.show()

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

        botonesGrafico(NORMAL)

    else:
        radio_buttonGraficos.config(state=DISABLED)
        radio_buttonEstadistics.config(state=DISABLED)
        radio_buttonDF.config(state=DISABLED)
        boton_conti.config(state=DISABLED)

        botonesGrafico(DISABLED)

#Actualizar mes
def addFechasMes(showData=True):
    global mes, mesDone 
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
        if showData:
            mesEntry.config(text=meses[mes-1])
    else:
        messagebox.showerror("Error", "Por favor asegurese de elegir un mes valido")

#Actualizar año
def addFechasAño(showData=True):
    global año, añoDone
    año = listboxAños.get()
    
    try:
        año=int(año)
    except ValueError:  #El año no es un número
        añoDone = False
    else:               #El año sí es un número
        if(showData):
            if año in yrs:
                añoDone = True
            else:
                añoDone = False
        else:
            añoDone = True
    
    if(añoDone):
        if showData:
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
        filtradoDeDatosForget()

#Filtrar datos check:
def checkButt():
    global checkbox_var, checkbox, labelAño, labelMes, mesEntry, añoEntry, buttonDone, yrs, listboxMeses, listboxAños
    
    yrs = dataFrame.getYearsList()   # Lista de años

    #Inh
    if habilitarFiltrado.get():

        listboxMeses = ttk.Combobox(root, values=meses)
        listboxAños =  ttk.Combobox(root,  values=yrs)


        radio_buttonGraficos.config(state=DISABLED)
        radio_buttonEstadistics.config(state=DISABLED)
        radio_buttonDF.config(state=DISABLED)
        boton_conti.config(state=DISABLED)

        if(elegirFuncion.get()==1):
            botonesGrafico(DISABLED)


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

        if(elegirFuncion.get()==1):
            botonesGrafico(NORMAL)

        try:
            checkbox.grid_forget()
            labelMes.grid_forget()
            labelAño.grid_forget()
            mesEntry.grid_forget()
            añoEntry.grid_forget()

            buttonDone.grid_forget()
            filtradoDeDatosForget()
        except: pass
        
#Mostrar opciones de uso del analísis de datos:
def showDataAnalisys():
    global habilitarFiltrado, elegirFuncion, habilitarGraf, radio_buttonGraficos, radio_buttonEstadistics, radio_buttonDF, botonFiltrado, boton_conti, botonGraf
    habilitarFiltrado = BooleanVar()
    
    elegirFuncion = IntVar()
    habilitarGraf = IntVar()

    botonFiltrado = Checkbutton(root, text="Filtrar datos",   variable=habilitarFiltrado, command=checkButt)
    botonFiltrado.grid(row=1, column=0, sticky='w')

    radio_buttonGraficos = Radiobutton(root, text="Gráficos", variable=elegirFuncion, value=1, command=chekOps)
    radio_buttonGraficos.grid(row=7, column=0, sticky='w')

    radio_buttonEstadistics = Radiobutton(root, text="Observar estádisticas", variable=elegirFuncion, value=2, command=botonesGraficoForget)
    radio_buttonEstadistics.grid(row=10, column=0, sticky='w')

    radio_buttonDF = Radiobutton(root, text="Ver data-frame", variable=elegirFuncion, value=3, command=botonesGraficoForget)
    radio_buttonDF.grid(row=11, column=0, sticky='w')

    #Boton de continuar:
    boton_conti = Button(root, text="Continuar", command=obtener_seleccion,fg="green", bg="white")
    boton_conti.grid(row=12, column=1, sticky="w")

def watch(locBin, window):
    global bins
    binEntry = locBin.get()
    try:
        locBinInt = int(binEntry)
    except:
        messagebox.showerror("Error", "Asegurese de que el valor sea un número entero")
    else:
        messagebox.showinfo("Exito", "Se hizo el cambio existosamente.")

        bins = locBinInt
        window.destroy()

#Preguntar al usuario si desea cambiar los grids del histograma:
def askGrid():
    global bins

    answer = messagebox.askyesno("Cambiar bins", "¿Desea cambiar el número predeterminado de divisiones?")
    if answer:
        nueva_ventana= Toplevel()
        nueva_ventana.resizable(False, False)

        nueva_ventana.iconbitmap("iconos/icon.ico")

        binsAsk=Entry(nueva_ventana, width=20)
        binsAsk.insert(0, "Cantidad de divisiones")  # Insertar el texto inicial en la entrad
        binsAsk.pack()
        continuar = Button(nueva_ventana, text="Continuar", bg="green", fg="white",  command= lambda: watch(binsAsk, nueva_ventana), width=15)
        continuar.pack()
    else:
        bins = dataFrame.hist.__defaults__[1]

#Elegir tipo de gráfico a desplegar:
def chekOps():
    global botonPlot, botonAll, botonBox, botonPie, botonCat, botonHist, tipoGrafico

    tipoGrafico = IntVar()

    botonPlot   = Radiobutton(root, text="Transacciones en función del tiempo",    variable=tipoGrafico, value=1, fg="green")
    botonPlot.grid(row=8, column=1, sticky="W")

    botonPie    = Radiobutton(root, text="Gasto por categoría %",         variable=tipoGrafico, value=2, fg="green")
    botonPie.grid(row=8, column=2, sticky="W")

    botonBox    = Radiobutton(root, text="Diagrama de caja",            variable=tipoGrafico, value=3, fg="green")
    botonBox.grid(row=9, column=1, sticky="W")

    botonCat    = Radiobutton(root, text="Gasto por categoría Núm",      variable=tipoGrafico, value=4, fg="green")
    botonCat.grid(row=9, column=2, sticky="W")

    botonHist    = Radiobutton(root, text="Histograma de gastos",        variable=tipoGrafico, value=5, fg="green", command=askGrid)
    botonHist.grid(row=8, column=3, sticky="W")

    botonAll    = Radiobutton(root, text="todos",                       variable=tipoGrafico, value=6, fg="green")
    botonAll.grid(row=9, column=3, sticky="W")

#%%Añadir datos manualmente

#Aactualizar días disponibles en función del mes seleccionado
def actualizarDia(event):
    mesEscogido=listboxMeses.get()
    
    if mesEscogido not in meses:
        listboxDia['values'] = list(range(1, 32))
    else:
        mesEscogido=meses.index(mesEscogido)
        listboxDia['values'] = list(range(1,nDiasMeeses[mesEscogido]+1))

#Guardar datos manualmente en el registro
def guardar_datos(condition):
    addFechasMes(condition)
    addFechasAño(condition)

    diaDone  = False
    montoDone = False
    
    miMes = str(mes)
    miAño = str(año)
    listboxDia['values'] = list(range(1, 32))

    miDia = listboxDia.get()
    monto = entry_monto.get()
    concepto = entry_concepto.get()
    categoria = listboxCategoria.get()

    #Verificar que el monto es correcto:
    try:
        monto = float(monto)
    except:
        messagebox.showerror("Error", "Ingrese un monto valido")
    else:
        montoDone = True

    #Verificar que el día es correcto:
    try:
        miDia1=int(miDia)
    except:
        pass
    else:
        if(miDia1<=31 and miDia1>=1):
            diaDone =True

    if (diaDone):
        if miDia1<10:
            miDia="0"+miDia
    else:
        messagebox.showerror("Error", "Ingrese un día valido")

    
    if(mesDone):
        if int(mes)<10:
            miMes="0"+miMes


    if(añoDone and mesDone and diaDone and montoDone):
        fecha = f"{miAño}-{miMes}-{miDia}"
        miSTR= f"{fecha},{concepto},{monto},{categoria}\n"
        
        try:
            #Guardar en archivo
            with open("Registro.csv", 'a') as archivo:
                archivo.write(miSTR)
        except:
            messagebox.showerror("Error", "No se pudo guardar en el archivo.")
        else:
            messagebox.showinfo("Realizado", "Sus datos fueron correctamente guardados.")


#%% Funciones para las opciones del menú

#Abrir nuevo archivo manualmente:  #TODO:
def habilitarFiltrado():
    cerrar_ventanas()
    clearBeginScreen()
    abrirArchivo()

#Abrir registro:
def chooseFunc(myDf=None):
    cerrar_ventanas()
    clearBeginScreen()

    global dataFrame

    if myDf==None:
        dataFrame=processData(archivo="Registro.csv")
    else:
        dataFrame = myDf
    showDataAnalisys()

#Añadir dato manualmente al registro:
def añadirDato():
    cerrar_ventanas()
    clearBeginScreen()
    global  entry_monto, entry_concepto, guardado, listboxMeses, listboxDia, listboxAños, listboxCategoria

    # Extraer el año de la fecha actual
    año_actual = dt.datetime.now().year

    # Crear etiquetas y campos de entrada para cada dato
    label_mes = Label(root, text="Mes:")
    listboxMeses = ttk.Combobox(root, values=meses)


    label_dia = Label(root, text="Día:")
    listboxDia = ttk.Combobox(root, values=list(range(1, 31+1)))

    label_anio = Label(root, text="Año:")
    listboxAños =  ttk.Combobox(root,  values=list(range(2000, año_actual+1)))

    label_categoria = Label(root, text="Categoría:")
    listboxCategoria = ttk.Combobox(root, values=categoria)

    label_monto = Label(root, text="Monto:")
    entry_monto = Entry(root)

    label_concepto = Label(root, text="Concepto:")
    entry_concepto = Entry(root)

    # Asociar la función de actualización al evento de selección del primer ComboBox
    listboxMeses.bind("<FocusOut>", actualizarDia)
    listboxMeses.bind("<Return>", actualizarDia)

    # Botón para guardar los datos
    boton_guardar = Button(root, text="Guardar", command=lambda:guardar_datos(False))

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

#%% WIDGET MANAGEMENT:
##-----------------------------------------------------------------------------------------------------------------------------------------------------
def cerrar_ventanas():
    # Función para cerrar todas las ventanas Toplevel
    for widget in root.winfo_children():
        if isinstance(widget, Toplevel):
            widget.destroy()

def update_datetime():
    current_datetime = dt.datetime.now()
    current_date = current_datetime.strftime('•Fecha: %Y-%m-%d')
    current_time = current_datetime.strftime('•Hora: %H:%M:%S %p')

    date_label.config(text=current_date)
    time_label.config(text=current_time)

    root.after(1000, update_datetime)
#Habilitar o inhabilitar los botones para la opción de gráficos
def botonesGrafico(miEstado):
    try:
        botonPlot.config(state=miEstado)
        botonPie.config (state=miEstado)
        botonBox.config (state=miEstado)
        botonCat.config (state=miEstado)
        botonHist.config (state=miEstado)
        botonAll.config (state=miEstado)
    except: pass
#Borrar existencia de los botones de elección de gráfico
def botonesGraficoForget():
    try:
        botonPlot.grid_forget()
        botonPie.grid_forget()
        botonBox.grid_forget()
        botonCat.grid_forget()
        botonHist.grid_forget()
        botonAll.grid_forget()
    except: pass

#Borrar existencia de los widgets de filtrado por fecha
def filtradoDeDatosForget():
    myLabel0.grid_forget()
    myLabel1.grid_forget()
    listboxMeses.grid_forget()
    listboxAños.grid_forget()
    buttonDates1.grid_forget()
    buttonDates2.grid_forget()

# Función para salir de la aplicación
def rst():
    cerrar_ventanas()
    clearBeginScreen()
    coin.grid(row=0,column=0, padx=10, pady=10)
    date_label.grid(row=1, column=0, sticky="w")
    time_label.grid(row=2, column=0, sticky="w")


#Borrar todos los widgets de la patalla
def clearBeginScreen():
    for widget in root.winfo_children():
        if widget !=menu_opciones and widget !=boton_rst:
            widget.grid_forget()


#Verificar la exsitencia de determinado widget
def widget_exists(widget):
    try:
        widget.winfo_exists()
        return True
    except:
        return False

#Manejar el gif de la pantalla de inicio
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

#%% MAIN:
##-----------------------------------------------------------------------------------------------------------------------------------------------------

root= Tk()
root.title("Hayek's app")
root.iconbitmap("iconos/icon.ico")


# Crear un menú
menu_principal = Menu(root)


root.config(menu=menu_principal)

# Crear un menú desplegable "Opciones"
menu_opciones = Menu(menu_principal)
menu_principal.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Abrir registro", command=chooseFunc)
menu_opciones.add_command(label="Abrir archivo", command=habilitarFiltrado)
menu_opciones.add_command(label="Añadir dato al registro manual", command=añadirDato)


# Crear un menú desplegable "Editar"
menu_opciones = Menu(menu_principal)
menu_principal.add_cascade(label="Editar", menu=menu_opciones)
menu_opciones.add_command(label="Guardar nuevo concepto", command=guardarConcepto)
menu_opciones.add_command(label="Eliminar concepto", command=eliminarConcepto)
menu_opciones.add_command(label="Reiniciar registro de conceptos", command=lambda: borrar_contenido_archivo("conceptosGuardados.txt"))
menu_opciones.add_command(label="Reiniciar contenido del registro", command=lambda: borrar_contenido_archivo("Registro.csv"))

#Calculadora:
calculadora = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Abrir calculadora", menu=calculadora)
calculadora.add_command(label="Abrir calculadora", command=calculator)



# Agregar una opción para reiniciar el programa
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=root.destroy)

# Botón de continuar:
boton_rst = Button(root, text="Reiniciar", command=rst,fg="green", bg="white")
boton_rst.grid(row=12, column=0, sticky="w", pady=10, padx=5)

image = Image.open("coin.gif")
#logo = Image.open('logo.png')

foto = ImageTk.PhotoImage(image)
# Crear un widget de etiqueta para mostrar la imagen
coin = Label(root, image=foto)
coin.grid(row=0,column=0, padx=10, pady=10)
# Inicia el ciclo de actualización del GIF
actualizar_gif(0)

#TODO:
#myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Etiqueta para mostrar la hora


# Etiqueta para la fecha
date_label = Label(root, font=('Bahnschrift', 16), foreground='black')
date_label.grid(row=1, column=0, sticky="w")

# Etiqueta para la hora
time_label = Label(root, font=('Bahnschrift', 16),  foreground='black')
time_label.grid(row=2, column=0, sticky="w")


# Iniciar la actualización de la fecha y hora
update_datetime()

root.mainloop()

