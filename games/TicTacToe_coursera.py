#Para hacer las jugadas de la computadora
import random

#El tablero es una matriz de strings
tablero = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"],
]
#Lista de 2 jugadores, el indice 1 es la persona, el indice 2 la computadora
jugadores = ["","Python"]

#Saber si el elemento pasado como argumento esta vacio
def elementoVacio(A, B):
    #el elemento esta vacio
    if tablero[A,B] == "_":
        return True
    else:
        #el elemento no esta vacio
        return False

def ingresaNombre():
    nombre = ""
    while (len(nombre)<3):
        print("Ingresa tu nickname de al menos 3 caracteres:")
        nombre = input().upper()
    #print("Bienvenido al juego ", nombre)
    return nombre

#El jugador elije que letra quiere ser
def ingresaLetra():
    letra = ""
    while not (letra == "X" or letra =="O"):
        print("Elejir X u O:")
        letra = input().upper()
    if letra == "X":
        list = ["X","O"]
        return list
    else:
        list = ["O","X"]
        return list

def quienPrimerTurno():
    # Elejir al azar quien tiene el primer turno
    if random.randint(1,2) == 1:
        return 1
    else:
        return 2


def dibujarTablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(str(tablero[i][j]))

#Determina el estado el juego
#Si se recorre el
def estadosJuego():
    #Si alguna vez nos salimos de este loop significa que no hubo "_" en la matriz
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "_":
                if i == 0 and j == 0:
                    #El juego acaba de comenzar
                    return False, True
                else:
                    #El juego, ya habia comenzado y sigue en curso
                    return True, False

    if jugarDenuevo():
        #El juego se reinicia
        return True, True
    else:
        #El juego se termina
        return False, False

def jugarDenuevo():
        respuesta = ""
        while not (respuesta == "SI" or respuesta == "NO"):
            print("Elejir SI o NO:")
            respuesta = input().upper()
        if respuesta == "SI":
            return True
        else:
            return False

def juegoComienza():
    nombre = ingresaNombre()
    letras = ingresaLetra()
    turno = quienPrimerTurno()
    return (nombre, letras, turno)

def juegoReinicia(nombre):
    nombre = nombre
    letras = ingresaLetra()
    turno = quienPrimerTurno()
    return (nombre, letras, numero)

def elejirJugada(jugadas_disponibles):
    jugada = 0
    while not (jugada == range(jugadas_disponibles)):
        print("Elejir 1-9:")
        jugada = input().int()
        return jugada

def bienvenidoJugador(datos):
    print(datos)
    print("Bienvenido: ", datos[0], "tu letra es: ", datos[1][0])
    if int(datos[2]) == 2:
        print("La computadora tiene el primer turno.")
    else:
        print("Tu tienes el primer turno.")

def jugadaComputadora(jugadas_disponibles):
    jugada = random.choice(jugadas_disponibles)
    return jugada

def hacerJugada(jugadas_disponibles, list_jugadas, tablero, jugada):
    pos = list_jugadas[jugada]
    print(pos)
    tablero[pos[0]][pos[1]] = "X"
    list_jugadas[jugada].remove()
    jugadas_disponibles[jugada].remove()
    print(jugadas_disponibles)
    print(list_jugadas)
    jugada = 0
    return jugadas_disponibles, list_jugadas, tablero, jugada
    
#Ideas
#Hacer el dibujo en la matriz
#Relacionar la lista de jugadas disponibles con la lista de posiciones y quitar el elemento
#Revisar si el elemento esta disponible
#

def logicaGeneral(quien_juega, jugadas_disponibles, list_jugadas, tablero, letra_compu):
    dibujarTablero(tablero)
    #logicaGeneral(quien_juega, jugadas_disponibles, list_jugadas, datos, letra_compu)
    if quien_juega == 2:
        jugada = jugadaComputadora(jugadas_disponibles)
        quien_juega = 1
    else:
        jugada = elejirJugada(jugadas_disponibles)
        quien_juega = 2
    jugadas_disponibles, list_jugadas, tablero, jugada = hacerJugada(jugadas_disponibles, list_jugadas, tablero, jugada)
    return quien_juega, jugadas_disponibles, list_jugadas, tablero

list_jugadas = (
[ 0 , 0 ],
[ 0 , 1 ],
[ 0 , 2 ],
[ 1 , 0 ],
[ 1 , 1 ],
[ 1 , 2 ],
[ 2 , 0 ],
[ 2 , 1 ],
[ 2 , 2 ],
)

jugadas_disponibles = (1,2,3,4,5,6,7,8,9)

while True:
    if (estadosJuego() == (False, False)):
        print("El juego termina.")
        break
    elif (estadosJuego() == (False, True)):
        print("El juego comienza.")
        datos = juegoComienza()
        nombre = datos[0]
        letra_compu = datos[1][1]
        letra_jugador = datos[1][0]
        quien_juega = datos[2]
        bienvenidoJugador(datos)
        print(quien_juega)

        quien_juega, jugadas_disponibles, list_jugadas, tablero = logicaGeneral(quien_juega, jugadas_disponibles, list_jugadas, tablero, letra_compu)

        print(quien_juega)
    elif (estadosJuego() == (True, True)):
        print("El juego comienza nuevamente.")
        datos = juegoReinicia(nombre)
        nombre = datos[0]
        letra_compu = datos[1][1]
        letra_jugador = datos[1][0]
        quien_juega = datos[2]
        bienvenidoJugador(datos)
        quien_juega, jugadas_disponibles, list_jugadas, tablero = logicaGeneral(quien_juega, jugadas_disponibles, list_jugadas, tablero, letra_compu)
    elif (estadosJuego() == (False, True)):
        dibujarTablero()
        #Usé esto para generar la variable list_jugadas
        #for i in range(len(tablero)):
            #for j in range(len(tablero[i])):
                #print("[",i,",",j,"]")
        jugada_actual = list_jugadas()
        test = input()
        #while not elementoVacio(A,B):
    else:
        print("Error en los estados de juego")
