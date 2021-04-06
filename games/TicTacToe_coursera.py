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
        return ["X","O"]
    else:
        return ["O","X"]

def primerTurno():
    # Elejir al azar quien tiene el primer turno
    if random.randint(0,20) >= 10:
        return 1
    else:
        return 2


def dibujarTablero(tablero):
    for i in range(len(tablero)):
        print ("|"),
        for j in range(len(tablero[i])):
            print (i*j," - |").format(str(tablero[i][j])),
            print("|")

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
    letra = ingresaLetra()
    turno = str(primerTurno())
    return (nombre, letra, turno)

def juegoReinicia():
    nombre = nombre
    letra = ingresaLetra()
    turno = str(primerTurno())
    return (nombre, letra, numero)

def elejirJugada():
    while not (jugada == range(1,9)):
        print("Elejir 1-9:")
        jugada = input().int()
        return jugada

def bienvenidoJugador(datos):
    print("Bienvenido: ", datos[0], "tu letra es: ", datos[1])
    if int(datos[2]):
        print("La computadora tiene el primer turno.")
    else:
        print("Tu tienes el primer turno.")

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

while True:
    if (estadosJuego() == (False, False)):
        print("El juego termina.")
        break
    elif (estadosJuego() == (False, True)):
        print("El juego comienza.")
        datos = juegoComienza()
        bienvenidoJugador(datos)
    elif (estadosJuego() == (True, True)):
        print("El juego comienza nuevamente.")
        datos = juegoReinicia()
        bienvenidoJugador(datos)
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
