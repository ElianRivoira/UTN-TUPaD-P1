# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")

# Actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

# Actividad 3
num = int(input("Ingrese un número par: "))
if num % 2 == 0:
  print("El número es par")
else:
  print("Por favor ingrese un número par")

# Actividad 4
edad = int(input("Ingrese su edad: "))
esNino = edad < 12 and edad >= 0
esAdolescente = edad >= 12 and edad < 18
esAdultoJoven = edad >= 18 and edad < 30
esAdulto = edad >= 30

if esNino:
  print("Es niño")
elif esAdolescente:
  print("Es adolescente")
elif esAdultoJoven:
  print("Es adulto joven")
elif esAdulto:
  print("Es adulto")
else:
  print("Edad no válida")

# Actividad 5
password = input("Ingrese su contraseña: ")
passLength = len(password)
if passLength < 8 or passLength > 14:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
  print("Ha ingresado una contraseña correcta")

#  Actividad 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

es_sesgo_positivo = media > mediana and mediana > moda
es_sesgo_negativo = media < mediana and mediana < moda
sin_sesgo = media == mediana and mediana == moda

if es_sesgo_positivo:
  print(f"Distribución sesgada a la derecha - moda: {moda}, mediana: {mediana}, media: {media}")
elif es_sesgo_negativo:
  print(f"Distribución sesgada a la izquierda - moda: {moda}, mediana: {mediana}, media: {media}")
elif sin_sesgo:
  print(f"Distribución simétrica - moda: {moda}, mediana: {mediana}, media: {media}")

# Actividad 7
string = input("Ingrese una cadena de texto: ")
ultimo_caracter = string[len(string)-1]
es_vocal = ultimo_caracter.lower() in ["a", "e", "i", "o", "u"]
if es_vocal:
  print(f"{string}!")
else:
  print(string)

# Actividad 8
nombre = input("Ingrese su nombre: ")
print("¿Cómo querés que se muestre tu nombre?")
print("1. En mayúsculas (ej: PEDRO)")
print("2. En minúsculas (ej: pedro)")
print("3. Con la primera letra mayúscula (ej: Pedro)")
opcion = input("Ingrese una opción (1, 2 o 3): ")

match opcion:
  case "1":
    print(nombre.upper())
  case "2":
    print(nombre.lower())
  case "3":
    print(nombre.title())
  case _:
    print("Opción no válida")

# Actividad 9
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))
muy_leve = 0 <= magnitud_terremoto < 3
leve = 3 <= magnitud_terremoto < 4
moderado = 4 <= magnitud_terremoto < 5
fuerte = 5 <= magnitud_terremoto < 6
muy_fuerte = 6 <= magnitud_terremoto < 7
extremo = magnitud_terremoto >= 7
if muy_leve:
  print("Terremoto categoria 'muy leve' en la escala de Richter")
elif leve:
  print("Terremoto categoria 'leve' en la escala de Richter")
elif moderado:
  print("Terremoto categoria 'moderado' en la escala de Richter")
elif fuerte:
  print("Terremoto categoria 'fuerte' en la escala de Richter")
elif muy_fuerte:
  print("Terremoto categoria 'muy fuerte' en la escala de Richter")
elif extremo:
  print("Terremoto categoria 'extremo' en la escala de Richter")

# Actividad 10
def es_bisiesto(anio):
  return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_estacion(hemisferio, mes, dia):
  # Definimos la fecha como una tupla para facilitar las comparaciones
  fecha = (mes, dia)

  #  Si la fecha esta entre el 21 de diciembre y el 20 de marzo, es invierno en el hemisferio norte y verano en el sur
  if (fecha >= (12, 21) or fecha <= (3, 20)):
    return "Invierno" if hemisferio == "N" else "Verano"
  # Si la fecha esta entre el 21 de marzo y el 20 de junio, es primavera en el hemisferio norte y otoño en el sur
  elif (fecha >= (3, 21) and fecha <= (6, 20)):
    return "Primavera" if hemisferio == "N" else "Otoño"
  # Si la fecha esta entre el 21 de junio y el 20 de septiembre, es verano en el hemisferio norte y invierno en el sur
  elif (fecha >= (6, 21) and fecha <= (9, 20)):
    return "Verano" if hemisferio == "N" else "Invierno"
  # Si la fecha esta entre el 21 de septiembre y el 20 de diciembre, es otoño en el hemisferio norte y primavera en el sur
  elif (fecha >= (9, 21) and fecha <= (12, 20)):
    return "Otoño" if hemisferio == "N" else "Primavera"

# Mapeo de nombres de meses a números
meses = {
  "enero": 1,
  "febrero": 2,
  "marzo": 3,
  "abril": 4,
  "mayo": 5,
  "junio": 6,
  "julio": 7,
  "agosto": 8,
  "septiembre": 9,
  "octubre": 10,
  "noviembre": 11,
  "diciembre": 12
}

# Días por mes (febrero se ajusta luego según si es bisiesto)
dias_por_mes = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

# Convertir mes a número
def convertir_mes_numero(mes_input):
  if mes_input.isdigit():
    return int(mes_input)
  else:
    return meses.get(mes_input)

# Input de hemisferio del usuario con validaciones
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
hemisferio_invalido = hemisferio not in ["N", "S"]
while hemisferio_invalido:
  hemisferio = input("Hemisferio inválido. Usá 'N' para norte o 'S' para sur.").strip().upper()
  hemisferio_invalido = hemisferio not in ["N", "S"]

# Input de mes del usuario con validaciones
mes_input = input("¿Qué mes es? (puede ser nombre o número): ").strip().lower()
mes = convertir_mes_numero(mes_input)
mes_invalido = not mes or mes < 1 or mes > 12
while mes_invalido:
  mes_input = input("Mes inválido. Ingresá un número del 1 al 12 o un nombre válido: ").strip().lower()
  mes = convertir_mes_numero(mes_input)
  mes_invalido = not mes or mes < 1 or mes > 12

# Input de fecha del usuario
anio = int(input("¿Qué año es?: "))
dia = int(input("¿Qué día es? (1-31): "))

# Ajustar días de febrero si es bisiesto
if es_bisiesto(anio):
  dias_por_mes[2] = 29

max_dia = dias_por_mes[mes]

if dia < 1 or dia > max_dia:
  print(f"Día inválido para el mes seleccionado. Ese mes tiene como máximo {max_dia} días en el año {anio}.")
else:
  estacion = obtener_estacion(hemisferio, mes, dia)
  print(f"Estás en {estacion}.")
