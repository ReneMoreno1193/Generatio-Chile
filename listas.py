"""Lista"""

frutasFeria = ["Zanahoria", "Naranajas", "Manzanas"]
print(frutasFeria[:2])

"""Modificar lista """
frutasFeria[2] = "pera"
print(frutasFeria)


"""Append agrega un elemento a lsita """

frutasFeria.append("Platano")
print(frutasFeria)


frutasFeria.append("Platano, frutilla")
print(frutasFeria)
frutasFeria.remove("Platano")
print(frutasFeria)


"""Tuplas"""

diasDeSemana = ("Lunes", "Martes", "Miércoles",
                "Jueves", "Viernes", "Sábado", "Domingo")
print(diasDeSemana[2])


"""Diccionario"""

librosYautores = {
    "Roberto Bolaño": "Detectives Salvajes",
    "Jorge Luis Borges": "Ficciones",
    "Las noches blancas": "Dostoievski"
}
print(librosYautores)

print(librosYautores["Jorge Luis Borges"])

"""Agregar valor y elementos a diccionarios"""
librosYautores["Nicanor Parra"] = "Poemas y antipoemas"

print(librosYautores)
