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
                return True

def calculo_diagonales(tablero, ficha):
    n_filas = len(tablero)
    n_columnas = len(tablero[0])
    #Derecha <--
    for c in range(n_columnas-3):
        for r in range(n_filas-1, 2, -1):
            if tablero[r][c] == ficha and tablero[r-1][c+1] == ficha and tablero[r-2][c+2] == ficha and tablero[r-3][c+3] == ficha:
                return True

    #Izquierda -->
    for c in range(n_columnas-1, 2, -1):
        for r in range(n_filas-1, 2, -1):
            if tablero[r][c] == ficha and tablero[r-1][c-1] == ficha and tablero[r-2][c-2] == ficha and tablero[r-3][c-3] == ficha:
                return True

def detector_ganador(tablero, ficha):
    return calculo_vertical(tablero, ficha) or calculo_horizontal(tablero, ficha) or calculo_diagonales(tablero, ficha)

tablero = crear_tablero(8, 10)
turno = "O"
sig_turno = "X"

while True:
    print("\n"*50)
    turno = sig_turno
    mostrar_tablero(tablero)
    print("")
    if turno == "X":
        columna = int(input("Ingese en que columna caerá su ficha (X): "))
        sig_turno = "O"
    elif turno == "O":
        columna = int(input("Ingese en que columna caerá su ficha (O): "))
        sig_turno = "X"
    tablero = jugada_tablero(tablero, columna, turno)
    if detector_ganador(tablero, turno):
        print("\n"*50)
        print("Has ganado jugador: ", "1" if turno == "X" else "2")
        mostrar_tablero(tablero)
        break

