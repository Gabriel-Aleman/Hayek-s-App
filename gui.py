from tkinter import *

root= Tk()
root.title("Hayek's app")
root.iconbitmap("icon.ico")


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