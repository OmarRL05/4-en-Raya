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
            print(objeto, end='  ')

#Pruebas de función
tablero = crear_tablero(7, 6)
mostrar_tablero(tablero)

def jugada_tablero(tablero, columna, ficha):
    if columna >= len(tablero[0]) or columna < 0:
        print("Error: La columna exede los parametros definidos.")
        return
    elif tablero[0][columna] != '.':
        print("Error: La columna esta llena.")
        return
    else:
        for fila in range(len(tablero)-1, -1, -1):
            if tablero[fila][columna] == '.':
                tablero[fila][columna] = ficha
                return tablero

#Pruebas de función
print("\n"*2)
tablero = jugada_tablero(tablero, 3, "X")
tablero = jugada_tablero(tablero, 2, "X")
tablero = jugada_tablero(tablero, 1, "X")
tablero = jugada_tablero(tablero, 0, "X")
mostrar_tablero(tablero)

def calculo_horizontal(tablero, ficha):
    n_filas = len(tablero)
    n_columnas = len(tablero[0])
    for r in range(n_filas):
        for c in range(n_columnas-3):
            if tablero[r][c] == ficha and tablero[r][c+1] == ficha and tablero[r][c+2] == ficha and tablero[r][c+3] == ficha:
                return True

def calculo_vertical(tablero, ficha):
    n_filas = len(tablero)
    n_columnas = len(tablero[0])
    for c in range(n_columnas):
        for r in range(n_filas-3):
            if tablero[r][c] == ficha and tablero[r+1][c] == ficha and tablero[r+2][c] == ficha and tablero[r+3][c] == ficha:
                print("11111")
                return True