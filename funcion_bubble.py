# Bubble Sort
def bubble_sort(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if matriz[j][1] > matriz[j + 1][1]: #ordenado por el segundo indice (vitamina)
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]


