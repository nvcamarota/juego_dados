"""
JUEGO DE DADOS CON CALLBACKS Y LAMBDAS
Objetivo: Crear un juego de dados donde el jugador lanza dos dados y se suman sus resultados, usando funciones callback para comportamientos basados en los resultados y lambdas para simplificar el código.
Instrucciones:
• Función para lanzar dados: Crear lanzar_dados que simule el lanzamiento de dos dados (números aleatorios entre 1 y 6) y devuelva sus resultados.
• Comportamientos:
• callback_ganar: Si la suma es 7, imprime "¡Ganaste!"
• callback_perder: Si la suma es 2 o 12, imprime "¡Perdiste!"
• callback_retirar: Si la suma es 3, 4, 5, 9, 10 u 11, imprime "Puedes retirar tu apuesta."
• Funciones para jugar: Crea jugar que acepte una función callback, lance los dados y ejecute el callback con los resultados.
• Lambdas:
• callback_dobles: Si los dos dados son iguales, imprime "¡Dobles!"
"""

import random

# Función que simula el lanzamiento de dos dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función para jugar, que acepta un callback
def jugar(callback):
    dado1, dado2 = lanzar_dados()
    suma = dado1 + dado2
    print(f"Lanzaste los dados: {dado1} y {dado2} (Suma: {suma})")
    callback(dado1, dado2, suma)

# Callback para cuando el jugador gana
def callback_ganar(dado1, dado2, suma):
    if suma == 7:
        print("¡Ganaste!")

# Callback para cuando el jugador pierde
def callback_perder(dado1, dado2, suma):
    if suma == 2 or suma == 12:
        print("¡Perdiste!")

# Callback para cuando el jugador puede retirar su apuesta
def callback_retirar(dado1, dado2, suma):
    if suma in [3, 4, 5, 9, 10, 11]:
        print("Puedes retirar tu apuesta.")

# Lambda para cuando los dados son dobles con condición ternaria
callback_dobles = lambda dado1, dado2, suma: print("¡Dobles!") if dado1 == dado2 else None

# Ejemplo de cómo jugar con diferentes callbacks
print("Juego con callback_ganar:")
jugar(callback_ganar)

print("\nJuego con callback_perder:")
jugar(callback_perder)

print("\nJuego con callback_retirar:")
jugar(callback_retirar)

print("\nJuego con callback_dobles:")
jugar(callback_dobles)

