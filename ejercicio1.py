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