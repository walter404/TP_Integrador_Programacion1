def quick_sort(matriz, columna):
    if len(matriz) <= 1:
        return matriz
    pivote = matriz[0]
    menores = []
    mayores = []

    for fila in matriz[1:]:
        if fila[columna] <= pivote[columna]:
            menores.append(fila)
        else:
            mayores.append(fila)

    return quick_sort(menores, columna) + [pivote] + quick_sort(mayores, columna)