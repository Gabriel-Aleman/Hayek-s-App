import os
from fileManagement import *
ruta_archivo_pdf = "C:/Users/gabri/OneDrive/Escritorio/Proyecto eléctrico/archivos/Promerica - 110833328_8_2023.PDF"
#a= openWithPumbler(ruta_archivo_pdf)
a=createDataFrame(ruta_archivo_pdf, "PROMERICA")
print(a)