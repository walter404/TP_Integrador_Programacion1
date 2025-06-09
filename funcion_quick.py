#quick Sort
def quick_sort(matriz):
    if len(matriz) <= 1:
        return matriz
    pivote = matriz[0]
    menores = []
    mayores = []

    for fila in matriz[1:]:
        if fila[2] <= pivote[2]:  #ordena por el precio indice 2
            menores.append(fila)
        else:
            mayores.append(fila)

    return quick_sort(menores) + [pivote] + quick_sort(mayores)