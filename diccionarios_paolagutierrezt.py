#practica 1 diccionarios
print(" ")
print("Gutierrez Torres Paola")
print(" ")

divisas =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

opcion = str(input("¿Que divisa quiere ingresar?\n"))
opcion = opcion.title()

if opcion in divisas:
    print(divisas[opcion])
else:
    print("no se encontro la divisa")