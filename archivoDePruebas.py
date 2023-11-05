import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
data = np.random.randn(1000)

# Calcular frecuencias relativas en porcentaje
frecuencia, bins, _ = plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
frecuencia_porcentaje = (frecuencia / len(data)) * 100

# Graficar el histograma con frecuencias relativas en porcentaje
plt.ylabel('Frecuencia Relativa (%)')  # Etiqueta del eje y
plt.show()
