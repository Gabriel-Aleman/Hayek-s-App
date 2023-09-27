# Crear una lista de ejemplo
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Definir el rango que deseas eliminar utilizando índices negativos (por ejemplo, eliminar los últimos 3 elementos)
indice_inicio = -3
indice_fin = -1

# Calcular los índices positivos equivalentes
indice_inicio = len(mi_lista) + indice_inicio
indice_fin = len(mi_lista) + indice_fin

# Eliminar el rango especificado de la lista original
del mi_lista[indice_inicio:indice_fin+1]

# La lista original ahora contiene los elementos sin el rango especificado
print(mi_lista)
