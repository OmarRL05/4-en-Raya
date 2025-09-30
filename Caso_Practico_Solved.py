tablero_header = [("0", "1", "2", "3", "4", "5", "6")]
jugador=1
finalizar=0


def table_starter(tablero_header):
    tablero = tablero_header
    for columna in tablero_header[0][:-1]:
        tablero = tablero + [[".", ".", ".", ".", ".", ".", ".",]]
    return tablero
tablero = table_starter(tablero_header)
movimiento = tablero

def mostrar_tablero(tablero):
    for fila in tablero[:]:
        print(fila)
        if fila is tablero[0]: print("===================================")

def columnas_calculador(tablero):
    columna_contador_x = [0, 0, 0, 0, 0, 0, 0]
    columna_contador_0 = [0, 0, 0, 0, 0, 0, 0]
    fin = 0
    i = 6
    j = 0
    #Recorrido de las filas de la matríz
    for fila in tablero[:0:-1]:
        #Recorrido por los elementos de la fila para añadir al contador
        for columna in fila[:][:]:
            #Condiciones para reiniciar contador cuando ya no hay igualdad de columnas por fila
            if i == 6: pass
            else:
                if columna_anterior != columna:
                    if columna_anterior == "x":
                        columna_contador_x[j] = 0
                    elif columna_anterior == "0":
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
    #Reconocer y Guardar al ganador del juego
    if 4 in columna_contador_x or columna_contador_0:
        if 4 in columna_contador_x:
            fin = 1
            ganador = "El ganador es el Jugador 1"
            print(ganador)
        elif 4 in columna_contador_0:
            fin = 1
            ganador = "El ganador es el Jugador 2"
            print(ganador)
    else:
        fin = 0
    return fin

def filas_calculador(tablero):
    pass
    filas_contador_x = [0, 0, 0, 0, 0, 0, 0]
    filas_contador_0 = [0, 0, 0, 0, 0, 0, 0]
    fin = 0 #Fin del Juego = 1 -> True
    i = 6 #Índice de la fila
    j = 0 # Índice de la columna
    #Recorrido de las filas de la matriz
    interruptor = True
    valor_columna1 = "."
    for fila in tablero[:0:-1]:
        #Recorrido de los elementos de la fila
        for columna in fila[:][:]:
            if interruptor:
                if columna != "." and columna == "x":
                    filas_contador_x[j] = 1
                elif columna != "." and columna == "0":
                    filas_contador_0[j] = 1

                if columna == valor_columna1: #if -> Compara la columna actual con la columna anterior, ej; columna(1)= "x" == columna(0) = "x"
                    if valor_columna1 == "x": #if -> En caso de ser iguales los valores, este if reconocerá cual es ese valor, si es X o 0.
                        filas_contador_x[j] = 1 + filas_contador_x[j-1]
                        #Explicación
                        '''
                        Nota: 
                                -Este filas_contador_x hace lo siguiente:
                                [0, 1, 0, 0] -> Suponiendo que esta fue la segunda iteración, donde se econtró que
                                                índice 0 no tenia un valor "x" pero el índice 1 si.
                                -En la siguiente iteración habrá una "x" en el índice 2, por lo que la expresión:
                                "filas_contador_x[j] +=1 +filas_contador_x[j-1]", hará lo siguiente:
                                                Estamos en j = 2
                                                [0, 1, 0, 0] -> [1] se encuentra en j=1. Para determinar el valor de j=2
                                                                harémos lo siguiente, [j=1]=1 + 1
                                                [0, 1, 2, 0] -> De esta manera se acumulan los elementos consecutivos 
                                                                del mismo tipo en las filas.
                        '''
                    elif valor_columna1 == "0":
                        filas_contador_0[j] = 1 + filas_contador_0[j-1]
                elif columna != valor_columna1:
                    #Si se rómpe la racha, el elemento se reinicia y la sumatoria vuelve a iniciar desde 0 en ese índice.
                    #Ejemplo ["x", "x", "x", "0", "x", "x"] ->[1, 2, 3, 0, 1, 2]
                    if valor_columna1 == "x":
                        filas_contador_x[j] = 0
                    elif valor_columna1 == "0":
                        filas_contador_0[j] = 0
            else:
                if columna == valor_columna1: #if -> Compara la columna actual con la columna anterior, ej; columna(1)= "x" == columna(0) = "x"
                    if valor_columna1 == "x": #if -> En caso de ser iguales los valores, este if reconocerá cual es ese valor, si es X o 0.
                        filas_contador_x[j] = 1 + filas_contador_x[j-1]
                        #Explicación
                        '''
                        Nota: 
                                -Este filas_contador_x hace lo siguiente:
                                [0, 1, 0, 0] -> Suponiendo que esta fue la segunda iteración, donde se econtró que
                                                índice 0 no tenia un valor "x" pero el índice 1 si.
                                -En la siguiente iteración habrá una "x" en el índice 2, por lo que la expresión:
                                "filas_contador_x[j] +=1 +filas_contador_x[j-1]", hará lo siguiente:
                                                Estamos en j = 2
                                                [0, 1, 0, 0] -> [1] se encuentra en j=1. Para determinar el valor de j=2
                                                                harémos lo siguiente, [j=1]=1 + 1
                                                [0, 1, 2, 0] -> De esta manera se acumulan los elementos consecutivos 
                                                                del mismo tipo en las filas.
                        '''
                    elif valor_columna1 == "0":
                        filas_contador_0[j] = 1 + filas_contador_0[j-1]
                elif columna != valor_columna1:
                    #Si se rómpe la racha, el elemento se reinicia y la sumatoria vuelve a iniciar desde 0 en ese índice.
                    #Ejemplo ["x", "x", "x", "0", "x", "x"] ->[1, 2, 3, 0, 1, 2]
                    if valor_columna1 == "x":
                        filas_contador_x[j] = 0
                    elif valor_columna1 == "0":
                        filas_contador_0[j] = 0
                #Al Terminar la iteración [valor_columna1] toma el valor de la columna con la que se trabajo para
                #compararla con la siguiente columna en la siguiente iteración.
            valor_columna1 = columna
            j += 1
        interruptor = False
        j= 0
        i-=1
        # Reconocer y Guardar al ganador del juego
    if 4 in filas_contador_x or filas_contador_0:
        if 4 in filas_contador_x:
            fin = 1
            ganador = "El ganador es el Jugador 1"
            print(ganador)
        elif 4 in filas_contador_0:
            fin = 1
            ganador = "El ganador es el Jugador 2"
            print(ganador)
    else:
        fin = 0
    return fin


def turno(jugador, tablero, ):
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
        for columna in fila[:][fila_sel]:
            #Comprobación de valor
            if "." in columna:
                print("JUGADA REALIZADA!")
                finalizar = True
                tablero[i][fila_sel] = jugada
                break
            elif columna is (["x"] or ["0"]):
                pass

        if finalizar:
            break
        i -= 1

    #Cambiar de jugador automaticamente para el proximo turno
    if jugador == 1: jugador = 0
    else: jugador = 1

    return tablero, jugador

#Simulación del juego
for i in range(20):

    if finalizar == 1:
        print("\n" * 25)
        print("FIN DEL JUEGO")
        columnas_calculador(movimiento)
        filas_calculador(movimiento)
        mostrar_tablero(movimiento)
        break
    print("\n"*25)
    print("Siguiente Jugador: ")
    movimiento, jugador= turno(jugador, tablero)


    finalizar_por_fila = filas_calculador(movimiento)
    finalizar_por_col = columnas_calculador(movimiento)
    if (finalizar_por_fila or finalizar_por_col) == 1:
        if finalizar_por_fila == 1: finalizar = finalizar_por_fila
        elif finalizar_por_col == 1: finalizar = finalizar_por_col



