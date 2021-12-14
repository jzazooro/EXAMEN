# EXAMEN

Mi direccion de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/jzazooro/EXAMEN.git)
https://github.com/jzazooro/EXAMEN.git

Hemos programado dos ejercicios: el segundo consise en un juego que comienza con seis fichas en un tablero 3x3 pero en posiciones aleatorias(3fichas cada jugador). Las fichas se mueven solo verticalmente, tantas posiciones como quieran, hemos programado esto respetando los turnos de los dos jugadores, que son dos IAs, ademas si una de los dos jugadores no puede mver ninguna de sus fichas habrá perdido. Por lo meno se tiene que poder realizar un movimiento.
En el ejercicio 1 aunque no he sabido como programarlo, pero deberiamos haber separado las letras de la palabra banana en cadenas de caracteres, y ver cuantas se pueden formar que empiecen por vocal, y cuantas por consonante, cuantas mas veces se repitan en la palabra banana, mas puntos daran.

ejercicio2:
```import random

fichasblancas='B'
fichasnegras='N'
tablero=[
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def imprimirtablero(cont):
    print(str(cont),end='')
    print(" tablero:")
    for i in range(3):
        print(' ')
        for j in range(3):
            print(tablero[j][i],end='')
    print()

def colocarfichasinicialmente():
    global tablero
    global fichasblancas
    global fichasnegras
    #vamos a colocar las fichas negras en el tablero
    situadas=0
    
    
    
ejercicio1:
def minion_game (cadena):
    puntuacionstuart = 0
    puntuacionkevin = 0
    vocal = 'aeiouAEIOU'
    for i in range (len(cadena)):
        if cadena[i] not in vocal:
            puntuacionstuart += (len(cadena))
        else: 
            puntuacionkevin += (len(cadena))
    print ("La puntuación de Stuart es " + str(puntuacionstuart) + "y la puntuación de Kevin es " + puntuacionkevin)
    if puntuacionstuart > puntuacionkevin:
        print ("Ganador, Stuart")
    elif puntuacionstuart < puntuacionkevin:
        print ("Ganador, Kevin")
    else:
        print ("Empate (' ') ")
if __name__ == "_main_":
    cadena = input ("Escoja una palabra: ")
    minion_game(cadena)


    while(situadas<3):
        ale1=random.randint(0, 2)
        ale2=random.randint(0, 2)
        if(tablero[ale1][ale2]==' '):
            tablero[ale1][ale2]=fichasnegras
            situadas=situadas+1
    #vamos a situar las fichas blancas en el tablero
    situadas=0

    while(situadas<3):
        ale1=random.randint(0, 2)
        ale2=random.randint(0, 2)
        if(tablero[ale1][ale2]==' '):
            tablero[ale1][ale2]=fichasblancas
            situadas=situadas+1

def posibilidaddemover(i,j):
    global tablero
    jf=-1

    if(j==0 and tablero[i][1]==' '):
        jf=1
    elif(j==1 and tablero[i][2]==' '):
        jf=2
    elif(j==1 and tablero[i][0]==' '):
        jf=0
    elif(j==2 and tablero[i][1]==' '):
        jf=1
    
    return jf

def movimiento(i,j,jf,ficha):
    global tablero

    tablero[i][jf]=ficha
    tablero[i][j]=' '

def movimientofichasnegras():
    global tablero
    global fichasnegras
    buscar=True
    i=0
    j=0

    while(buscar==True):
        if(tablero[i][j]==fichasnegras):
            jf=posibilidaddemover(i,j)
            if(jf!=-1):
                movimiento(i,j,jf,fichasnegras)
                buscar=False #ya hemos movido
        if(buscar==True):
            j=j+1
            if(j==3):
                j=0
                i=i+1
                if(i==3):
                    break #no hemos movido
    return buscar

def movimientofichasblancas():
    global tablero
    global fichasblancas
    buscar=True
    i=0
    j=0

    while(buscar==True):
        if(tablero[i][j]==fichasblancas):
            jf=posibilidaddemover(i,j)
            if(jf!=-1):
                movimiento(i,j,jf,fichasblancas)
                buscar=False #ya han movido
        if(buscar==True):
            j=j+1
            if(j==3):
                j=0
                i=i+1
                if(i==3):
                    break #no hemos movido
    return buscar




def main():
    i=1
    partidafinalizada=False
    inicio=random.randint(0, 1)
    print("Para elegir quien empieza a jugar, se escogerá un numero aleatorio")
    print("un numero aleatorio entre el 0 y el 1 (0=empiezan negras, 1=empiezanblancas).")
    print("El numero seleccionado ha sido el: ", inicio)
    colocarfichasinicialmente()
    imprimirtablero(1)
    if(inicio==0):
        while(partidafinalizada==False):
            if(movimientofichasnegras()==True): #no ha movido
                partidafinalizada=True
        if(movimientofichasblancas()==True): #no ha movido
            partidafinalizada=True
        i=i+1
        imprimirtablero(i)
        quedeseas=input('¿Desea seguir viendo la partida(S/N)?: ')
        if(quedeseas=='n' or quedeseas=='N'):
            partidafinalizada=True
        else:
            print("la partida continua")

    elif(inicio==1):
        while(partidafinalizada==False):
            if(movimientofichasblancas()==True): #no ha movido
                partidafinalizada=True
            if(movimientofichasnegras()==True): #no ha movido
                partidafinalizada=True
            i=i+1
            imprimirtablero(i)
            quedeseas=input('¿Desea seguir viendo la partida?(S/N): ')
            if(quedeseas=='n' or quedeseas=='N'):
                partidafinalizada=True
            else:
                print("la partida continua")




if __name__=="__main__":
    main()
