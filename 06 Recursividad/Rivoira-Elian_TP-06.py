# Ejercicio 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("El número debe ser positivo.")
else:
    for i in range(1, numero + 1):
        print(f"El factorial de {i} es {factorial(i)}")

# Ejercicio 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero_fibonacci = int(input("Ingrese la posición en la serie de Fibonacci: "))
if numero_fibonacci < 0:
    print("La posición debe ser un número entero no negativo.")
else:
    print("Serie de Fibonacci:")
    for i in range(numero_fibonacci + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

# Ejercicio 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente. Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

# Ejercicio 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un número entero positivo en base decimal: "))
if numero_decimal < 0:
    print("El número debe ser positivo.")
else:
    binario = decimal_a_binario(numero_decimal)
    if binario == "":
        binario = "0"
    print(f"La representación en binario de {numero_decimal} es: {binario}")

# Ejercicio 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # Convertir la palabra a minúsculas para evitar problemas de mayúsculas/minúsculas
    palabra = palabra.lower()
    
    # Caso base: si la longitud es 0 o 1, es un palíndromo
    if len(palabra) <= 1:
        return True
    
    # Comparar el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    
    # Llamada recursiva eliminando el primer y último carácter
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra o frase sin espacios ni tildes: ")
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")

# Ejercicio 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# No se puede convertir el número a string.

def suma_digitos(n):
    # Caso base: si n es 0, la suma de los dígitos es 0
    if n == 0:
        return 0
    else:
        # Sumar el último dígito (n % 10) y llamar recursivamente con el resto del número (n // 10)
        return (n % 10) + suma_digitos(n // 10)
    
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("El número debe ser positivo.")
else:
    print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# Ejercicio 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

def contar_bloques(n):
    # Caso base: si n es 0, no hay bloques
    if n <= 0:
        return 0
    else:
        # Sumar el número de bloques en el nivel actual (n) y llamar recursivamente para el siguiente nivel (n - 1)
        return n + contar_bloques(n - 1)

numero_bloques = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
if numero_bloques < 0:
    print("El número de bloques debe ser un entero positivo.")
else:
    print(f"El total de bloques necesarios para construir la pirámide es: {contar_bloques(numero_bloques)}")

# Ejercicio 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito del número es igual al dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9): "))
if numero < 0 or digito < 0 or digito > 9:
    print("El número debe ser positivo y el dígito debe estar entre 0 y 9.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
