import time
import random
from funcion_quick import quick_sort
from funcion_bubble import bubble_sort
from funcion_busqueda_binaria import busqueda_binaria

#Generar matriz aleatoria con números   
matriz = []
def generar_productos(cantidad):
    for _ in range(cantidad):
        nombre = f"Producto{random.randint(1, 100)}"
        vitamina = random.choice(['A', 'B', 'C', 'D', 'E'])
        precio = random.randint(100, 1000)
        matriz.append([nombre, vitamina, precio])
    return matriz

matriz = generar_productos(100)

# Copias para ordenar
matriz_bubble = matriz.copy()
matriz_quick = matriz.copy()

# Ordenamientos bubble sort por nombre
inicio_bubble = time.time()
bubble_sort(matriz_bubble)
fin_bubble = time.time()

#ordenamiento quick sort por precio
inicio_quick = time.time()
matriz_quick = quick_sort(matriz_quick)
fin_quick = time.time()

# Mostrar ordenamientos
print("Ordenado con Bubble Sort:")
for fila in matriz_bubble:
    print(fila)
print(f"Tiempo Bubble Sort: {fin_bubble - inicio_bubble:.6f} segundos\n")

print("Ordenado con Quick Sort:")
for fila in matriz_quick:
    print(fila)
print(f"Tiempo Quick Sort: {fin_quick - inicio_quick:.6f} segundos\n")

# Búsqueda binaria por nombre
buscar = matriz_bubble[1][1] # Buscar el primer nombre como ejemplo
inicio_busqueda = time.time()
indice = busqueda_binaria(matriz_bubble, buscar, 1)
fin_busqueda = time.time()

if indice != -1:
    print(f"'{buscar}' encontrado en la posición {indice}: {matriz_bubble[indice]}")
else:
    print(f"'{buscar}' no encontrado.")
print(f"Tiempo búsqueda binaria: {fin_busqueda - inicio_busqueda:.6f} segundos")

# Búsqueda binaria por precio
buscar_precio = matriz_quick[-1][2] # Buscar el precio más alto como ejemplo
inicio_busqueda = time.time()
indice = busqueda_binaria(matriz_quick, buscar_precio, 2)
fin_busqueda = time.time()

# Mostrar resultado
if indice != -1:
    print(f"'{buscar_precio}' encontrado en la posición {indice}: {matriz_quick[indice]}")
else:
    print(f"'{buscar_precio}' no encontrado.")
print(f"Tiempo búsqueda binaria: {fin_busqueda - inicio_busqueda:.6f} segundos")