"""Ciclo for"""

lista = ["Diccionario", 23, 24, True, 45.5]

"""for [variable de iteración] + in + nombre de la variable"""

for x in lista:
    print(f"Elemento {x}")

"""Imprime solo los numeros pares"""
numeros = [2, 45, 19, 13, 178]
for numero in numeros:

    if numero % 2 == 2:
        print(numero)