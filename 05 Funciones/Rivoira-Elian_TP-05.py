# Actividad 1: Crear una lista con los múltiplos de 4 del 1 al 100.
print("Actividad 1: Crear una lista con los múltiplos de 4 del 1 al 100.")
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


# Actividad 2: Crear una lista con cinco elementos y mostrar el penúltimo.
print("Actividad 2: Crear una lista con cinco elementos y mostrar el penúltimo.")
lista = ["pizza", "chocolate", "helado", "café", "hamburguesa"]
print(f"El penúltimo elemento es: {lista[-2]}")


# Actividad 3: Crear una lista vacía, agregar tres palabras con append e imprimirla.
print("Actividad 3: Crear una lista vacía, agregar tres palabras con append e imprimirla.")
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("Python")
print(lista_vacia)


# Actividad 4: Reemplazar el segundo y último valor de la lista "animales".
print("Actividad 4: Reemplazar el segundo y último valor de la lista 'animales'.")
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


# Actividad 6: Crear una lista con números del 10 al 30 en saltos de 5 y mostrar los dos primeros.
print("Actividad 6: Crear una lista con números del 10 al 30 en saltos de 5 y mostrar los dos primeros.")
lista_numeros = list(range(10, 31, 5))
print(f"Los dos primeros son: {lista_numeros[:2]}")


# Actividad 7: Reemplazar los dos valores centrales de la lista "autos".
print("Actividad 7: Reemplazar los dos valores centrales de la lista 'autos'.")
autos = ["cronos", "polo", "suran", "gol"]
autos[1:3] = ["civic", "sentra"]
print(autos)


# Actividad 8: Crear una lista vacía "dobles" y agregar el doble de 5, 10 y 15.
print("Actividad 8: Crear una lista vacía 'dobles' y agregar el doble de 5, 10 y 15.")
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)


# Actividad 9: Modificar la lista "compras".
print("Actividad 9: Modificar la lista 'compras'.")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


# Actividad 10: Crear una lista anidada.
print("Actividad 10: Crear una lista anidada.")
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)