tablero_header = [("0", "1", "2", "3", "4", "5", "6")]


def table_starter(tablero_header):
    tablero = tablero_header
    for columna in tablero_header[0][:-1]:
        tablero = tablero + [[".", ".", ".", ".", ".", ".", ".",]]
    return tablero
tablero = table_starter(tablero_header)

def mostrar_tablero(tablero):
    for fila in tablero[:]:
        print(fila)
        if fila is tablero[0]: print("===================================")

def turno(jugador, tablero):
    # Selección de ficha
    if jugador == 1: jugada = "x"
    else: jugada = "0"

    #UI / Jugada del jugador
    '''
    Notas:   -- Agregar función para la interfaz de jugador en esta area 
             -- Borrar mostrar tablero de aquí e incluirlo en la nueva función
    '''
    mostrar_tablero(tablero)

    #Input de la Jugada
    fila_sel = int(input("Seleccione la columna en donde caerá su ficha: "))

    # Input -> Error de Valor
    if (fila_sel < 0 or fila_sel > 6) :
        while fila_sel < 0 or fila_sel > 6 :
            print("Error: El valor que ingreso no es valido")
            fila_sel = int(input("Seleccione de nuevo la columna en donde caerá su ficha: "))

    #Input -> Apartado para comprobar si la columna no esta llena
    columna_llena = False
    if tablero[1][fila_sel] != ".": columna_llena = True
    while columna_llena is True:
        print("Error: La columna ya esta llena, pruebe con otro numero")
        fila_sel = int(input("Seleccione de nuevo la columna en donde caerá su ficha: "))
        if tablero[1][fila_sel] == ".": columna_llena = False

    fila_margen = fila_sel +1  #fila_margen sirve para...

    ## Registro en el tablero
    ## ====================== ->
    i = 6 #Contador de filas
    finalizar = False #Detecta cuando se encontró una localización valida para la ficha
    for fila in tablero[:0:-1]:
        print("Fila actual:", i)
        print("Contenido de la fila: ", fila)
        for columna in fila[:][fila_sel]:
            print("Columna: ", fila_sel)
            print("Contenido de la columna: ", columna)
            #Comprobación de valor
            if "." in columna:
                print("CAMBIO!")
                finalizar = True
                tablero[i][fila_sel] = jugada
                break
            elif columna is (["x"] or ["0"]):
                pass

        if finalizar:
            break
        i -= 1




    ## ====================== <-


    ## -- Meter la función que calcule si ya gano alguien y guardarlo en winner

    ## -- Agregar un if winner: break

    #Cambiar de jugador automaticamente para el proximo turno
    if jugador == 1: jugador = 0
    else: jugador = 1

    return tablero, jugador

def columnas_calculador(tablero):
    columna_contador_x = [0, 0, 0, 0, 0, 0, 0]
    columna_contador_0 = [0, 0, 0, 0, 0, 0, 0]
    i = 6
    j = 0
    #Recorrido de las filas de la matríz
    for fila in tablero[:0:-1]:
        print(fila)
        #Recorrido por los elementos de la fila para añadir al contador
        for columna in fila[:][:]:
            #Condiciones para reiniciar contador cuando ya no hay igualdad de columnas por fila
            if i == 6: pass
            else:
                if columna_anterior != columna:
                    print("CAMBIO!")
                    if columna_anterior == "x":
                        print("EN X")
                        columna_contador_x[j] = 0
                    elif columna_anterior == "0":
                        print("EN 0")
                        columna_contador_0[j] = 0

            #Aumentar contador
            if columna == "x":
                columna_contador_x[j] +=1
            elif columna == "0":
                columna_contador_0[j] +=1
            j+=1
            columna_anterior = columna

        j= 0
        i-=1
        print(columna_contador_x, columna_contador_0)

        #Reconocer y Guardar al ganador del juego
        if 4 in columna_contador_x or columna_contador_0:
            if 4 in columna_contador_x:
                print("El ganador es el Jugador 1")
                winner = "El ganador es el Jugador 1"
            elif 4 in columna_contador_0:
                print("El Ganador es el Jugador 2")
                winner = "El ganador es el Jugador 2"
            else: continue
    return

jugador=1
for i in range(20):
    break
    movimiento, jugador= turno(jugador, tablero)
    print("Siguiente Jugador")

tablero = [("0", "1", "2", "3", "4", "5", "6"),[".", ".", ".", ".", ".", ".", "x",], [".", ".", ".", ".", ".", ".", "x",], [".", "0", "0", "0", "0", "x", "x",], [".", "x", "0", "x", "0", "x", "x",] ]
columnas_calculador(tablero)