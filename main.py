
from fileManagement import *

bancos= ["BAC ahorro", "BAC cred", "BCR ahorros", "BCR cred", "PROMERICA"]

if __name__ == "__main__":
    while True:
        print("Archivos encontrados en la ruta predeterminada:")
        archivos = encontrarArchivos(ruta_carpeta)
        
        for i in range(len(archivos)):
            print(i+1,".",archivos[i])

        archivo     = int(input("\n Ingrese el archivo del que desea obtener información:"))
        archivos    = archivos[archivos-1]

        for i in range(len(bancos)):
            print(i+1,".",bancos[i])

        banco     = int(input("\n Ingrese el tipo de banco:"))
        banco     = bancos[banco-1]

        df = createDataFrame(ar, "BAC cred"    )    #DONE

        break