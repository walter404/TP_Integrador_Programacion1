# Búsqueda binaria

def busqueda_binaria(matriz, valor, columna):
    inicio = 0
    fin = len(matriz) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if matriz[medio][columna] == valor:
            return medio
        elif matriz[medio][columna] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1
