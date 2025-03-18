from pares_primos_gemelos import *
from primos_palindromicos import *

def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            limite = int(input("Ingrese el límite superior del rango: "))
            pares_gemelos = encontrar_pares_primos_gemelos(limite)
            print("Pares de números primos gemelos encontrados:")
            for par in pares_gemelos:
                print(par)
        elif opcion == "2":
            limite = int(input("Ingrese el límite superior del rango: "))
            primos_palindromicos = encontrar_primos_palindromicos(limite)
            print("Números primos palindrómicos encontrados:")
            for numero in primos_palindromicos:
                print(numero)
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu = """
Menu:

1. Encontrar pares de números primos gemelos
2. Encontrar números primos palindrómicos
3. Salir
"""

def mostrar_menu():
    print(menu)


