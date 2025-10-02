def crear_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ['.']*columnas
    return tablero