from random import *

nombre = input('Bienvenido, cual es tu nombre? ')
numero = randint(1, 100)
# print(numero)

print(f'\nBueno, {nombre}, he pensado un  numero entre 1 y 100, y tienes solo ocho intentos para '
      f'adivinar cuál crees que es el numero ')

# Contador de Intentos
intento = 0
adivina = 0

while intento < 8:
    adivina = int(input('\nDime tu numero: '))
    intento += 1

    if adivina < 1 or adivina > 100:
        print('\nLo siento, has elegido un numero que no esta permitido')

    elif adivina < numero:
        print('\nRespuesta incorrecta, el numero que ingresaste es menor al numero secreto')

    elif adivina > numero:
        print('\nRespuesta incorrecta, el numero que ingresaste es mayor al numero secreto')

    else:
        print(f'\nFelicidades {nombre}, acertaste el numero secreto. Te ha tomado {intento} intentos')
        break

if adivina != numero:
    print(f'Lo siento, intentos agotados, El numero secreto era {numero}.')
