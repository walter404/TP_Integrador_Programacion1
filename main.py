import time
from funcion_quick import quick_sort
from funcion_bubble import bubble_sort
from funcion_busqueda_binaria import busqueda_binaria


nombre = ['Manzana', 'Pera', 'Puerro', 'Kiwi', 'Sandia']
vitamina = ['A', 'B', 'C', 'D', 'E']
precios = ['1', '2', '3', '4', '5']

matriz = []

for i in range(len(nombre)):
    fila = [nombre[i], vitamina[i], precios[i]]
    matriz.append(fila)

# Copias para ordenar
matriz_bubble = matriz.copy()
matriz_quick = matriz.copy()

# Bubble Sort y tiempo
inicio_bubble = time.time()
bubble_sort(matriz_bubble, 0)  # Ordenar por nombre
fin_bubble = time.time()
print("Bubble Sort realizado.")
print(f"Tiempo: {fin_bubble - inicio_bubble:.6f} segundos\n")

# Quick Sort y tiempo
inicio_quick = time.time()
matriz_quick = quick_sort(matriz_quick, 0)
fin_quick = time.time()
print("Quick Sort realizado.")
print(f"Tiempo: {fin_quick - inicio_quick:.6f} segundos\n")

# Búsqueda binaria
buscar = "Pera"
inicio_busqueda = time.time()
indice = busqueda_binaria(matriz_quick, buscar, 0)
fin_busqueda = time.time()

if indice != -1:
    print(f"'{buscar}' encontrado en la posición {indice}.")
else:
    print(f"'{buscar}' no encontrado.")
print(f"Tiempo búsqueda binaria: {fin_busqueda - inicio_busqueda:.6f} segundos")