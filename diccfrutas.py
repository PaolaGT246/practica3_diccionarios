#practica 3 diccionarios
print(" ")
print("Gutierrez Torres Paola")
print(" ")

frutas = {"platano":"36","manzana":"27","naranja":"38","fresa":"50"}
opcion = str(input("¿que fruta quieres comprar?\n"))
kilos = float(input("¿cuantos kilos quieres llevar?\n"))

precios = kilos*(float(frutas[opcion]))

print(precios)