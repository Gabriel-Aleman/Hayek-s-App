import numpy as np
import matplotlib.pyplot as plt

# Datos
labels = np.array(['A', 'B', 'C', 'D'])
stats = np.array([20, 35, 30, 35])

# Número de variables
num_vars = len(labels)

# Ángulos para cada eje
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Asegurar que el gráfico sea cerrado
stats = np.concatenate((stats, [stats[0]]))
angles += angles[:1]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats, color='red', linewidth=2)

# Etiquetas tangenciales al círculo
for angle, label in zip(angles, labels):
    ax.text(angle, 40, label, ha='center', va='center', rotation=angle * 180/np.pi - 90)

# Mostrar el gráfico
plt.show()
