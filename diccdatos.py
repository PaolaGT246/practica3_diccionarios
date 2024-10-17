#practica 2 diccionarios
print(" ")
print("Gutierrez Torres Paola")
print(" ")

nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
direccion = input("ingrese su direccion: ")
numero = input("ingrese su numero: ")

datos = {"nombre":nombre, "edad":edad, "direccion":direccion, "numero":numero}
print(f"{datos ['nombre']} tiene {datos ['edad' ]} años, su direccion es {datos ['direccion']} y su numero de telefono es {datos ['numero']}")
print(" ")