# Bubble Sort
def bubble_sort(matriz, columna):
    n = len(matriz)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matriz[j][columna] > matriz[j + 1][columna]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
