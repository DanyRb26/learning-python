

''' 
Script Description

Cree una funcion que genere de dos dados (1-6)
 y que muestre  por pantalla el mendaje GANADOE cuando genere un par de SEIS, 
 de lo contraio, el mensaje dira, SIGUE INTENTANDO'''


#importar biblioteca para generar numeros aleatorios enteros.
from random import randint 

#Lanzar y generar los valores de los dos dados

def dices():
    dice1 = randint (1,6)
    dice2 = randint (1,6)

    return dice1, dice2

#Salidas impresion
d = dices()
d1 = d[0]
d2 = d[1]
print("Dices:",d)
print ("Dice 1:",d1)
print ("Dice 2:",d2)









#print ("Dice1", dice1)
#print ("Dice2", dice2)
