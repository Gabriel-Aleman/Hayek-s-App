#Librerias
#-----------------------------------------------------------------------------------------------------------------------------------------------------
import PyPDF2
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import pdfplumber
import datetime as dt

#Variables globales:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
ruta_carpeta = "/Users/gabri/OneDrive/Escritorio/PROYECTO/archivos"

#Funciones:
#-----------------------------------------------------------------------------------------------------------------------------------------------------


"""
encontrarArchivos: Función para ubicar los archivos con los que se pretende
trabajar.

inputs:
    -ruta: Carpeta en la que se deben buscar los archivos.
otputs:
    -archivos_en_carpeta: Lista con todos los archivos hallados en la
    carpeta.
"""
def encontrarArchivos(ruta):
    # Ruta de la carpeta que deseas explorar

    # Lista para almacenar los nombres de los archivos
    archivos_en_carpeta = []

    # Itera a través de los archivos y subdirectorios en la carpeta
    for carpeta_actual, subdirectorios, archivos in os.walk(ruta):
        for archivo in archivos:
            # Agrega el nombre del archivo a la lista
            archivos_en_carpeta.append(archivo)

    return archivos_en_carpeta

"""
readFile: Función para leer el contenido del archivo PDF

inputs:
    -fileName: Nombre del archivo.
    -page: Página a leer (predeterminado ninguna)
otputs:
    -texto: Contenido del archivo.
"""
def readFile(fileName, page=None): 
    #Crear un objeto "PDF"
    pdfFileObj = open(fileName, 'rb')
 
    #Crear un objeto para leer
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
 
    #Obtener el número de páginas
    numPags=len(pdfReader.pages)
 
    #Extraer el texto del documento
    texto=""
    if(page is None):
        for i in range(numPags):
            pageObj = pdfReader.pages[i]
            texto+=pageObj.extract_text()

    else:
        pageObj = pdfReader.pages[page-1]
        texto+=pageObj.extract_text()


    return texto

"""
openWithPumbler: Función para leer el contenido del archivo PDF

inputs:
    -fileName: Nombre del archivo.
    -page: Página a leer (predeterminado ninguna)
otputs:
    -texto: Contenido del archivo.
"""
def openWithPumbler(fileName, myPage=None):
    # Abre el archivo PDF
    texto=""
    with pdfplumber.open(fileName) as pdf:
        if(myPage is None):
        
                # Itera a través de las páginas del PDF
                for page in pdf.pages:
                    # Extrae el texto de la página
                    texto += page.extract_text()
        else:
            pagina_deseada = pdf.pages[myPage-1]
            texto = pagina_deseada.extract_text()
    return texto

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
filterText: Función para filtrar parte del texto.

inputs:
    -fileName: Nombre del archivo.
    -texto: Texto a filtrar
    -begin: Secuencia de inicio.
    -en: Secuencia de fin.
otputs:
    -string: texto filtrado.
"""

"""
elementosRepetidos: Función para eliminar elementos de una fila
de una columna.

inputs:
    -miMatriz: Matriz de entrada.
    -lenMat: Longitud que se quiere para cada fila.
    -indice_pred: Indice a partir del cula eliminar elementos
    (predeterminado -3).
otputs:
    -miMatriz1: La smatriz ya formateada.
"""
def elementosRepetidos(miMatriz, lenMat, indice_pred=-3):
    miMatriz1 = miMatriz
    for i in range(len(miMatriz1)):
        if (len(miMatriz1[i])>lenMat):
            # Definir el rango que deseas eliminar utilizando índices negativos (por ejemplo, eliminar los últimos 3 elementos)
            dif = len(miMatriz1[i])-lenMat
            indice_fin = indice_pred
            indice_inicio = indice_fin-dif+1

            # Calcular los índices positivos equivalentes
            indice_inicio = len(miMatriz1[i]) + indice_inicio
            indice_fin = len(miMatriz1[i]) + indice_fin

            # Eliminar el rango especificado de la lista original
            del miMatriz1[i][indice_inicio:indice_fin+1]

            # La lista original ahora contiene los elementos sin el rango especificado
    return miMatriz1


"""
reSizeMatrix: Función para eliminar columnas adicionales no deseadas
de una matriz.

inputs:
    -miMatriz: Matriz de entrada.
    -popIndex: Indice a partir del cual eliminar elementos (predeterminado -2)
otputs:
    -miMatriz1: La smatriz ya formateada.
"""
def reSizeMatrix(miMatriz, popIndex=-2):
    miMatriz1 = miMatriz
    minLen=len(miMatriz1[0])
    
    for element in miMatriz1:
        if(len(element)<minLen):
            minLen = len(element)
    
    for i in range(len(miMatriz1)):
        if(len(miMatriz1[i])>minLen):
            miMatriz1[i].pop(popIndex)
    
    return miMatriz1

"""
delSpace: Función para eliminar los espacios repetidos.

inputs:
    -MiString: Texto recibido.
    -dateIsTextLike: Especificar si la fecha utiliza caracterre
otputs:
    -original_string: La secuencia de caráteres ya formateada.
"""
def delSpace(MiString, dateIsTextLike):

    original_string = MiString
    string1 = list(original_string)
    modString = False
    k=0

    for i in range(len(string1)):
        if(string1[i].isalpha()):   #Se ha recibido una letra:
            if(not dateIsTextLike): #Revisar que la letra no corresponde a una fecha
                modString = True
            else:
                k+=1
                if(k==3):
                    dateIsTextLike =False
                continue

        if(modString):
            if (string1[i].isdigit() or string1[i] == "("):
                string1[i-1] = " "
                break
            
            elif(string1[i] == " "):
                string1[i] = "_"

    original_string = "".join(string1)
    return original_string


"""
filterText: Función para filtrar información especifíca de un texto.

inputs:
    -texto: Texto original.
    -begin: Secuencia de inicio.
    -end    Secuencia de fin.
outputs:
    -data: Texto filtrado.

"""
def filterText(texto, begin, end):
    string      = ""
    storeData   = False
    data        = ""

    #Analizar cada línea del texto:
    for element in texto:
        #Mientras no se terminado la línea, siga leyendo
        if(element!="\n"):  
            string += element

        #Se ha leido una línea completa:
        else:
            if(storeData):
                #Se recibio la secuencia de acabar:
                if(end in string):
                    storeData=False
                    data= data[:-1] #Eliminar último caracter de salto de línea
                    break
                #Añadir línea a la sección filtrada:
                else:
                    data+=(string+"\n")
                    
            #Se recibió la secuencia de inicio:
            if(begin in string):
                storeData= True

            string=""
    return data


"""
splitMyText: Función para filtrar información especifíca de un texto.

inputs:
    -texto: Texto original.
    -begin: Secuencia de inicio.
    -end    Secuencia de fin.
outputs:
    -data: Texto filtrado.

"""
def splitMyText(texto, dateIsTextLike = False, removeSpace = True, miSize=True):
    nuevoTexto = texto.split("\n") #Dividir en líneas
    #Iterar sobre cada string
    for i in range(len(nuevoTexto)):
        #Eliminar los espacios repetidos:
        nuevoTexto[i] = re.sub(r'\s+', ' ', nuevoTexto[i])

        #Eliminar espacios en secuencia de caracteres:
        if(removeSpace):
            nuevoTexto[i] = delSpace(nuevoTexto[i], dateIsTextLike)

        nuevoTexto[i] = nuevoTexto[i].split(" ")

    if(miSize):
        nuevoTexto = reSizeMatrix(nuevoTexto)

    return nuevoTexto 


"""
createDataFrame: Función para retornar al usuario un data frame con
los datos obtenidos.

inputs:
    -tipo: Tipo de archivo de donde se extraen los datos (predeterminado ninguno).
    -data: Matriz con toda la información.
outputs:
    -df: Data Frame a devolver con la información.

"""
def createDataFrame(archivo, tipo=None,):
    miArchivo     = "archivos/"+archivo  #Done

    match tipo:
        case "BAC ahorros":
            secunciaDeInicio    = "NO. REFERENCIA FECHA CONCEPTO DÉBITOS CRÉDITOS"
            secunciaDeFin       = "ÚLTIMA LÍNEA"

            textoArchivo    = openWithPumbler(miArchivo, myPage=3)
            textoFiltrado   = filterText(textoArchivo, secunciaDeInicio, secunciaDeFin)
            data            = splitMyText(textoFiltrado, dateIsTextLike=True)


            df = pd.DataFrame(data, columns=['Documento', 'Fecha contable', "Concepto", "Monto"])

        case "BAC cred":
            secunciaDeInicio    = "Saldo Anterior"
            secunciaDeFin       = "Desglose pagos del mes"

            textoArchivo    = openWithPumbler(miArchivo)
            textoFiltrado   = filterText(textoArchivo, secunciaDeInicio, secunciaDeFin)
            textoFiltrado   = splitMyText(textoFiltrado, dateIsTextLike=True, miSize=False)
            data            = elementosRepetidos(textoFiltrado, lenMat= 4)
            data.pop(0)

            df = pd.DataFrame(data, columns=['Documento', 'Fecha contable', "Concepto", "Monto"])

        case "BCR ahorros":
            secunciaDeInicio    = "Movimiento Contable"
            secunciaDeFin       = "Última línea"

            textoArchivo    = openWithPumbler(miArchivo)
            textoFiltrado   = filterText(textoArchivo, secunciaDeInicio, secunciaDeFin)
            data            = splitMyText(textoFiltrado)


            df = pd.DataFrame(data, columns=['Fecha de movimiento', 'Fecha contable', "Documento", "Concepto", "Número", "Monto"])

        case "BCR cred":
            secunciaDeInicio    = "Saldo anterior: : "
            secunciaDeFin       = "R E S U M E N -- D E L -- E S T A D O -- D E -- C U E N T A -- T A R J E T A - P R I N C I P A L"
            
            textoArchivo    = openWithPumbler(miArchivo)
            textoFiltrado   = filterText(textoArchivo, secunciaDeInicio, secunciaDeFin)
            textoFiltrado   = splitMyText(textoFiltrado,miSize=False)
            data            = elementosRepetidos(textoFiltrado, lenMat= 7)

            data.pop(0)
            df = pd.DataFrame(data, columns=[ 'Fecha de movimiento', 'Fecha contable',  "Número", "Concepto", 'Tasa', "Monto", "interes"])
        
        case "PROMERICA":
            secunciaDeInicio    = "XXXX-XXXX-XXXX-"
            secunciaDeFin       = "XXXX-XXXX-XXXX-"

            textoArchivo    = openWithPumbler(miArchivo)
            textoFiltrado   = filterText(textoArchivo, secunciaDeInicio, secunciaDeFin)
            textoFiltrado   = splitMyText(textoFiltrado)
            data            = elementosRepetidos(textoFiltrado, lenMat= 3, indice_pred=-2)


            df = pd.DataFrame(data, columns=['Fecha contable', 'Conceptos', "Monto"])
        case _:
            None

    return df

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
processData: Clase para procesar la información relativa a los datos del banco.

atributos:
    -df: Data frame con la información mínima (fehca, monto, concepto).
    -tipo: Clase de Banco (BCR cred, BCR ahorro, BAC cred, BAC ahorro o PROMERICA) 
    [predeterminado ninguno].
    -moneda: El tipo de moneda en que están los datos (Euro, Dolar, Colon, etc...)
    [predeterminado ninguno].
"""
class processData:
    def __init__(self, df, tipo=None, moneda=None):
        self.df     = df
        self.tipo   = tipo
        self.moneda = moneda

        #IDLE:
        self.formatdf()

    
    #formatdf: Atributo para eliminar inormación innecesaria
    #TODO: Cambiar el formato de las fechas.
    def formatdf(self):
        columnas_a_eliminar = []
        self.df = self.df.rename(columns={'Fecha contable': 'Fecha'})
        match self.tipo:
            case "BAC ahorros":
                columnas_a_eliminar = ['Documento']
            case "BAC cred":
                columnas_a_eliminar = ["Documento"]
            case "BCR ahorros":
                columnas_a_eliminar = ["Documento", "Fecha de movimiento", "Número"]
            case "BCR cred":
                columnas_a_eliminar = ["Número", "Fecha de movimiento", "Tasa", "interes"]
            case "PROMERICA":
                pass
            case _:
                pass
        
        self.df = self.df.drop(columnas_a_eliminar, axis=1)
        self.df['Monto'] = self.df['Monto'].str.replace(",", "")
        self.df['Monto'] = self.df['Monto'].astype(float)

    def formatDate(self):
        dates = self.df["Fecha"].tolist()
        datesStr = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
        newDates = []   
    
        if (self.tipo == "BAC ahorros" or self.tipo=="BAC  cred"):
            for date in dates:
                for i in range(12):
                    if(datesStr[i] in date):
                        date = date.replace(datesStr[i], str(i+1))
                        date = date.replace("-", "/")

                        newDates.append(date)
                        break
            self.df["Fecha"] = newDates

        
        match self.tipo:
            case _:
                print("Hola")

        year = dt.datetime.now().year
        self.df['Fecha'] = self.df['Fecha'].apply(lambda x: f'{year}/{x}')



    #createGraph: Atributo para crear un gráfico de los montos como función del tiempo.
    def createGraph(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.df['Fecha'], self.df['Monto'], align='center', color='blue')


        # Personaliza la gráfica
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.title('Evolución de monto con el tiempo')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Rotar las etiquetas del eje x para mejorar la legibilidad si es necesario
        plt.xticks(rotation=45)

        # Muestra la gráfica
        plt.show()
    
    #boxGraph: Atributo para crear un gráfico de caja.
    def boxGraph(self):
        # Crear el diagrama de caja para la columna "Datos"
        plt.figure(figsize=(8, 3))
        plt.boxplot(self.df['Monto'], vert=False)  # Utiliza vert=False para un diagrama de caja horizontal

        # Personaliza el gráfico
        plt.xlabel('Valor')
        plt.title('Diagrama de Caja para la Columna "Datos"')

        # Muestra el gráfico
        plt.show()
 
    def piePlot(self):

        plt.figure(figsize=(8, 8))
        conteo_categorias =self.df["Categorías"].value_counts()
        
        plt.pie(conteo_categorias, labels=conteo_categorias.index, autopct='%1.1f%%', startangle=140)
        plt.title('Diagrama de Pastel de Categorías')
        plt.axis('equal')  # Para asegurarse de que el gráfico sea circular
        plt.show()
    
    #stadistics: Atributo para obtener los resultados estadísticos.
    #outputs: 
    #   -estadisticas: Resultados estadiísticos.
    def stadistics(self):
        estadisticas = self.df['Monto'].describe()
        print(type(estadisticas))
        return estadisticas
        
    def guardar_csv(self, nombre_archivo="Registro"):
        # Guardar el DataFrame en un archivo CSV
        self.df.to_csv(nombre_archivo, mode='a', index=False)
        
#TestBench:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
misArchivos         = encontrarArchivos(ruta_carpeta)


# Create the pandas DataFrame
df1 = createDataFrame(misArchivos[0], "BAC ahorros" )    #DONE
df2 = createDataFrame(misArchivos[1], "BAC cred"    )    #DONE
df3 = createDataFrame(misArchivos[2], "BCR ahorros" )
df4 = createDataFrame(misArchivos[3], "BCR cred"    )         
df5 = createDataFrame(misArchivos[4], "PROMERICA"   )     

df1= processData(df1, "BAC ahorros")
df2= processData(df2, "BAC cred")
df3= processData(df3, "BCR ahorros")
df4= processData(df4, "BCR cred")
df5= processData(df5, "PROMERICA")


df1.formatDate()


# print dataframe.
print(df1.df, "\n")
print(df2.df, "\n")
print(df3.df, "\n")
print(df4.df, "\n")
print(df5.df, "\n")

