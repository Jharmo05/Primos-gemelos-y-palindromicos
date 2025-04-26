from primos_palindromicos import *
from es_primo import *

def encontrar_pares_primos_gemelos(limite):
    pares_gemelos = []
    for numero in range(2, limite):
        if es_primo(numero) and es_primo(numero + 2):
            pares_gemelos.append((numero, numero + 2))
    return pares_gemelos
