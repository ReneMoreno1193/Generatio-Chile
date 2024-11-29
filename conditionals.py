pais = input("Ingresa tu país: ").strip().lower()  # Normalizamos la entrada

if pais == "colombia":  # Comparación en minúsculas
    print("Hola parce")
elif pais == "chile":
    print("Wena poh")
elif pais == "venezuela":
    print("Hola chamo")
else:
    print("No eres de acá")


""" ejercicio propuesto """


numero_1 = (input("Ingresa el primer número: "))
nnmero_2 = (input("Ingresa el segundo número: "))
nnmero_3 = (input("Ingresa el tercer número: "))

if numero_1 > nnmero_2 and numero_1 > nnmero_3:
    print(f"El primer número {numero_1} es mayor que {nnmero_2} y {nnmero_3}")
elif nnmero_2 > numero_1 and nnmero_2 > nnmero_3:
    print(f"El número {nnmero_2} es mayor que {numero_1} y {nnmero_3}")
elif nnmero_3 > numero_1 and nnmero_3 > nnmero_2:
    print(f"El número  {nnmero_3} es mayor que el {numero_1} y {nnmero_2}")
else:
    print("Ingresa un numero positivo")
