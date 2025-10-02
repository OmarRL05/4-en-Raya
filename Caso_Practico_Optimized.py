def crear_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ['.']*columnas
    return tablero

def mostrar_tablero(tablero):
    for num in range(len(tablero[0])):
        """ Accede a la primera lista
            [".", ".", ".", "." ... n]
            len(tablero[0] toma la cantidad
            "n" de elementos en la lista.
        """
        print(num, end='  ')
    for fila in tablero:
        print("")
        for objeto in fila:
            print(objeto, "|", end=' ')
