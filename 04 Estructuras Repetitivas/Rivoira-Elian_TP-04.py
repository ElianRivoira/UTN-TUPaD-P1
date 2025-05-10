# Actividad 1: Imprimir números del 0 al 100 en orden creciente.
print("Actividad 1: Imprimir números del 0 al 100 en orden creciente.")
for i in range(101):
  print(i)


# Actividad 2: Solicitar un número entero y determinar la cantidad de dígitos.
print("Actividad 2: Solicitar un número entero y determinar la cantidad de dígitos.")
numero = input("Ingresa un número entero: ")
print(f"La cantidad de dígitos es: {len(numero)}")


# Actividad 3: Sumar todos los números entre dos valores dados, excluyendo esos valores.
print("Actividad 3: Sumar todos los números entre dos valores dados, excluyendo esos valores.")
inicio = int(input("Ingresa el valor inicial: "))
fin = int(input("Ingresa el valor final: "))
suma = sum(range(inicio + 1, fin))
print(f"La suma de los números entre {inicio} y {fin} es: {suma}")


# Actividad 4: Sumar números ingresados hasta que se ingrese un 0.
print("Actividad 4: Sumar números ingresados hasta que se ingrese un 0.")
total = 0
while True:
  numero = int(input("Ingresa un número (0 para terminar): "))
  if numero == 0:
    break
  total += numero
print(f"La suma total es: {total}")


# Actividad 5: Juego de adivinanza de un número aleatorio entre 0 y 9.
print("Actividad 5: Juego de adivinanza de un número aleatorio entre 0 y 9.")
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
  intento = int(input("Adivina el número (entre 0 y 9): "))
  intentos += 1
  if intento == numero_secreto:
    print(f"¡Acertaste en {intentos} intentos!")
    break


# Actividad 6: Imprimir números pares entre 0 y 100 en orden decreciente.
print("Actividad 6: Imprimir números pares entre 0 y 100 en orden decreciente.")
for i in range(100, -1, -2):
  print(i)


# Actividad 7: Calcular la suma de los números entre 0 y un número dado.
print("Actividad 7: Calcular la suma de los números entre 0 y un número dado.")
numero = int(input("Ingresa un número entero positivo: "))
suma = sum(range(numero + 1))
print(f"La suma de los números entre 0 y {numero} es: {suma}")


# Actividad 8: Contar pares, impares, positivos y negativos en 100 números ingresados.
print("Actividad 8: Contar pares, impares, positivos y negativos en 100 números ingresados.")
pares, impares, positivos, negativos = 0, 0, 0, 0
for _ in range(100):
  numero = int(input("Ingresa un número: "))
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1
  if numero > 0:
    positivos += 1
  elif numero < 0:
    negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")


# Actividad 9: Calcular la media de 100 números ingresados.
print("Actividad 9: Calcular la media de 100 números ingresados.")
suma = 0
for _ in range(100):
  numero = int(input("Ingresa un número: "))
  suma += numero
print(f"La media es: {suma / 100}")


# Actividad 10: Invertir los dígitos de un número ingresado.
print("Actividad 10: Invertir los dígitos de un número ingresado.")
numero = input("Ingresa un número: ")
print(f"El número invertido es: {numero[::-1]}") # Recorre el string desde el final hacia el inicio, mostrandolo 'invertido'
