
from fileManagement import *
from dataAnalisys import *

bancos= ["BAC ahorros", "BAC cred", "BCR ahorros", "BCR cred", "PROMERICA"]
categorias=["Entretenimiento", "Transporte", "Comida", "Otros"]

def showCateg(arr):
    for i in range(len(arr)):
        print(i+1,"-",arr[i])
              
if __name__ == "__main__":
    while True:
        print("Archivos encontrados en la ruta predeterminada:")
        archivos = encontrarArchivos(ruta_carpeta)
        
        for i in range(len(archivos)):
            print(i+1,".",archivos[i])

        archivo     = int(input("\n Ingrese el archivo del que desea obtener información:"))
        archivo    = archivos[archivo-1]

        for i in range(len(bancos)):
            print(i+1,".",bancos[i])

        banco     = int(input("\n Ingrese el tipo de banco:"))
        banco     = bancos[banco-1]

        miDataFrame = createDataFrame(archivo, banco)
        miDataFrame = processData(miDataFrame, banco)

        comuna_elementos = miDataFrame.df['Concepto'].tolist()
        
        misCateg=[]
        for i in comuna_elementos:
            print("Para el concepto",i, "Escoja una categoría.")
            showCateg(categorias)
            cat = int(input("Categoría: "))
            misCateg.append(categorias[cat-1])

        miDataFrame.addCategories(misCateg)
        
        print(miDataFrame.df)
        print("\n",miDataFrame.stadistics())

        miDataFrame.createGraph()
        miDataFrame.boxGraph()
        miDataFrame.piePlot()

        respuesta = input("¿Desea cerrar? Ingrese 1 para confirmar o cualquier otra tecla para continuar: ")
        if respuesta == '1':
            print("Cerrando...")
            break
        else:
            print("Continuando...")
