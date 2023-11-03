from fileManagement import *
import matplotlib.pyplot as plt
from numpy import pi, linspace, concatenate, degrees
import datetime as dt

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
    def __init__(self, df=None, tipo=None, archivo=None, moneda=None):
        self.df      = df
        self.section = df
        self.tipo    = tipo
        self.archivo = archivo
        self.moneda  = moneda

        #IDLE:
        if(self.tipo!=None):
            self.formatdf()
            self.formatDate()
            self.section=self.df

        elif(self.archivo!=None):
            self.cargar_csv()
            self.section = self.df
        else:
            print("CONFIGURACIÓN INVALIDA")

        
    #addCategories: Método para añadir categorias
    #inputs:
    #   -categories: Categorias a añadir
    def addCategories(self, categories):
        if (len(self.df) == len(categories)) and ("Categorias" not in self.df.columns): #Revisar que las categorías coinciden con el tamaño del DF
        # Agregar una nueva columna al DataFrame
            self.df['Categorias'] = categories

    #formatdf: Método para eliminar inormación innecesaria
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
        

    #formatDate: Método para que las fechas estén ordenadas y deacuerdo a lo deseado
    def formatDate(self):

        if(self.tipo!=None):
            dates = self.df["Fecha"].tolist()
            datesStr = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
            newDates = []   
            if (self.tipo == "BAC ahorros" or self.tipo=="BAC cred"):
                for date in dates:
                    for i in range(12):
                        if(datesStr[i] in date):
                            date = date.replace(datesStr[i], str(i+1))

                            newDates.append(date)
                            break
                self.df["Fecha"] = newDates

            
            if self.tipo== "BAC ahorros":
                year = dt.datetime.now().year
                self.df['Fecha'] = self.df['Fecha'].apply(lambda x: f'{year}/{x}')
                self.df['Fecha'] =  pd.to_datetime(self.df['Fecha'], format='%Y/%m/%d', errors='coerce')

            elif self.tipo== "BAC cred":
                self.df['Fecha'] =  pd.to_datetime(self.df['Fecha'], format='%d-%m-%y', errors='coerce')
            
            elif self.tipo == "PROMERICA":
                self.df['Fecha'] =  pd.to_datetime(self.df['Fecha'], format='%d/%m/%Y', errors='coerce')

            elif ("BCR" in self.tipo):
                self.df['Fecha'] =  pd.to_datetime(self.df['Fecha'], format='%d/%m/%y', errors='coerce')

            
        self.df = self.df.sort_values(by='Fecha', ascending=True)
        self.df = self.df.reset_index(drop=True)

    #chooseSegment: Metodo para elegir los datos a analizar, por mes y año
    #inputs:
    #    -mes: Mes a elegir
    #    -año: Año a elegir
    def chooseSegment(self, mes, año):
        self.df['Fecha'] = pd.to_datetime(self.df['Fecha'])
        #self.section = self.df[(self.df['Fecha'].dt.year == año) & (self.df['Fecha'].dt.month == mes)]
        self.section =self.df[(self.df['Fecha'].dt.year == año) & (self.df['Fecha'].dt.month == mes)]

    #stadistics: Método para obtener los resultados estadísticos.
    #outputs: 
    #   -estadisticas: Resultados estadiísticos.
    def stadistics(self):
        promedio = self.section['Monto'].mean()
        mediana = self.section['Monto'].median()
        desviacion = self.section['Monto'].std()
        min = self.section['Monto'].min()
        max = self.section['Monto'].max()
        sum = self.section['Monto'].sum()
        count = self.section['Monto'].count()
        
        # Crear una cadena con los resultados en líneas separadas
        results_string = f"-Cantidad de transacciones: {count}\n" \
                         f"-Total gastado: {sum}\n" \
                         f"-Mínimo gastado: {min}\n" \
                         f"-Máximo gastado: {max}\n" \
                         f"-Desviación Estándar: {desviacion}\n" \
                         f"-Mediana: {mediana}\n" \
                         f"-Promedio gastado:\n{promedio}"

        return results_string
    
    #getYearsList: Método para obtner una lista de los años de los que
    #se tiene regisro.
    #Outputs: 
    #       -años: lista con los años
    def getYearsList(self):
        self.df['Fecha'] = pd.to_datetime(self.df['Fecha'])
        años = set(self.df['Fecha'].dt.year)
        return list(años)
        

    #getMontList: Método para obtner una lista de los meses de los que
    #se tiene regisro.
    #Outputs: 
    #       -meses: lista con los años
    def getMonthList(self):
        self.df['Fecha'] = pd.to_datetime(self.df['Fecha'])
        meses = set(self.df['Fecha'].dt.month)
        return list(meses)
    
    #guardar_csv: Método para guardar los datos en un CSV
    #inputs: 
    #   -nombre_archivo: Archivo donde guardar los resultados
    def guardar_csv(self, nombre_archivo="Registro.csv"):

        #Revisar que ya se añadiéron las categorías:
        if "Categorias" in self.df.columns:
            # Guardar el DataFrame en un archivo CSV
            self.df.to_csv(nombre_archivo, mode='a', header=False, index=False)

    #cargar_csv: Método para cargar los datos al data frame
    def cargar_csv(self):
        column_names = ['Fecha', 'Concepto', "Monto", "Categorias"]
        # Cargar los datos del archivo CSV en un DataFrame
        self.df = pd.read_csv(self.archivo, names=column_names)
        self.df = self.df.sort_values(by='Fecha', ascending=True)
        self.df = self.df.reset_index(drop=True)
        
    #createGraph: Atributo para crear un gráfico de los montos como función del tiempo.
    def createGraph(self,  miTitulo='Evolución de transacciones con el tiempo'):
        df_agregado = self.section.groupby('Fecha')['Monto'].sum().reset_index()             #Sumar los gastos de cada fecha
        plt.plot(df_agregado['Fecha'], df_agregado['Monto'], marker='o', linestyle='-', color='b')
        plt.fill_between(df_agregado['Fecha'], df_agregado['Monto'], hatch='//', edgecolor='lightblue', facecolor='cyan')

        # Personaliza la gráfica
        plt.xlabel('Fecha')
        plt.ylabel('Valor')
        plt.title(miTitulo, fontweight='bold')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Rotar las etiquetas del eje x para mejorar la legibilidad si es necesario
        plt.xticks(rotation=20)

        # Muestra la gráfica
        plt.show()
    
    #boxGraph: Método para crear un gráfico de caja.
    def boxGraph(self, miTitulo='Diagrama de Caja para transacciones'):
        # Crear el diagrama de caja para la columna "Datos"
        plt.boxplot(self.section['Monto'], vert=False)  # Utiliza vert=False para un diagrama de caja horizontal

        # Personaliza el gráfico
        plt.xlabel('Valor')
        plt.title(miTitulo, fontweight='bold')

        # Muestra el gráfico
        plt.show()
    
    
    #categPlot: Método para crear un gráfico de pastel.
    def categPlot(self, miTitulo="Gasto por categorias", pie=True):

        conteo_categorias =self.section["Categorias"].value_counts()
        if(pie):
            plt.pie(conteo_categorias, labels=conteo_categorias.index, autopct='%1.1f%%', startangle=140)
            plt.title(miTitulo+" (%)", fontweight='bold')
            plt.axis('equal')  # Para asegurarse de que el gráfico sea circular

        else:
            categories = conteo_categorias.index
            values = conteo_categorias.values

            num_vars = len(categories)

            # Calcular los ángulos para el gráfico de radar
            angles = linspace(0, 2 * pi, num_vars, endpoint=False).tolist()

            # Asegurarse de que se cierre el gráfico
            values = concatenate((values, [values[0]]))
            angles += angles[:1]

            # Crear el gráfico de radar
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
            ax.fill(angles, values, color='green', alpha=0.25)

            # Agregar las etiquetas en cada ángulo
            ax.set_yticklabels([])
            ax.set_xticks(angles[:-1])
            
            # Rotar las etiquetas
            ax.set_xticklabels(categories, rotation=degrees(angles), fontsize=12)


            # Agregar las etiquetas con la cantidad de veces que se repite cada categoría en cada círculo
            # Etiquetar cada punto en el radar con el nombre del elemento y su cantidad
            for i, (label, count) in enumerate(zip(categories, values)):
                angle = angles [i]
                ax.plot(angle, count, marker='o', markersize=2, color='black')
                ax.text(angle, count-0.4, f'{count}', ha='center', va='center')

            plt.title(miTitulo+" (Núm)", fontweight='bold')
            ax.plot(angles, values, color='green', linewidth=1, linestyle='solid')

        plt.show()

        

    #hist: Atributo para crear histograma de las transacciones realizadas
    def hist(self, miTtitulo="Histograma de la columna de transacciones", defBins=5):
        # Graficar un histograma de la columna 'columna_de_datos'
        plt.hist(self.section['Monto'], bins=defBins)  # Cambia el número de bins según tu preferencia
        plt.xlabel('Gastos de transacciónes')
        plt.ylabel('Frecuencias')
        plt.title(miTtitulo)
        plt.grid()
        plt.show()
        


   
#TestBench:
#-----------------------------------------------------------------------------------------------------------------------------------------------------
"""misArchivos         = encontrarArchivos(ruta_carpeta)


import random
categorias=["Entretenimiento", "Transporte", "Comida", "Otros"]

# Create the pandas DataFrame
#df1 = createDataFrame(misArchivos[0], "BAC ahorros" )    #DONE
df2 = createDataFrame(misArchivos[1], "BAC cred"    )    #DONE
#df3 = createDataFrame(misArchivos[2], "BCR ahorros" )
#df4 = createDataFrame(misArchivos[3], "BCR cred"    )         
#df5 = createDataFrame(misArchivos[4], "PROMERICA"   )     

#df1= processData(df1, "BAC ahorros")
df2= processData(df2, "BAC cred")
#df3= processData(df3, "BCR ahorros")
#df4= processData(df4, "BCR cred")
#df5= processData(df5, "PROMERICA")
#array_aleatorio = random.choices(categorias, k=len(df5.df))
#df5.addCategories(array_aleatorio)
#df5.guardar_csv()

# print dataframe.
#print(df1.df, "\n")
#print(df2.df, "\n")
#print(df3.df, "\n")
#print(df4.df, "\n")
#print(df5.df, "\n")


#dff=processData(archivo="Registro.csv")
#año_deseado = 2023
#mes_deseado = 8
#dff.chooseSegment(8, 2023)

cat = [ random.choice(categorias) for _ in range(len(df2.section))]
print(cat)
df2.addCategories(cat)
df2.createGraph()
df2.boxGraph()
df2.categPlot()

#print(df2.df)
#
#print(dff.getYearsList())
#print(dff.getMonthList())
#
#print(dff.section)"""