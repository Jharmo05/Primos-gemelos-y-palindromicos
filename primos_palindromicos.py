from pares_primos_gemelos import *
from es_primo import *

def es_palindromico(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def encontrar_primos_palindromicos(limite):
    primos_palindromicos = []
    for numero in range(10, limite):
        if es_primo(numero) and es_palindromico(numero):
            primos_palindromicos.append(numero)
    return primos_palindromicos