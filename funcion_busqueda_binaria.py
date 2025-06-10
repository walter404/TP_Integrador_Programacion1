# Búsqueda binaria
def busqueda_binaria(matriz, valor, columna):
    inicio = 0
    fin = len(matriz) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = matriz[medio][columna]
        if str(actual).lower() == str(valor).lower(): # devolvemos posicion
            return medio
        elif str(actual).lower() < str(valor).lower():# menor, buscamos en la mitad derecha
            inicio = medio + 1
        else:
            fin = medio - 1 # mayor, buscamos mitad izquierda
    return -1 

