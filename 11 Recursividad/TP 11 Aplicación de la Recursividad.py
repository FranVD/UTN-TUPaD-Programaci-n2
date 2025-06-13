#TP 11: Aplicación de la Recursividad 
#Autor: Reynoso Arellano, Franco Gastón


# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Mostrar factoriales del 1 al número ingresado
num = int(input("Ingrese un número para calcular sus factoriales: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique. 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#Mostrar la serie completa hasta la posición dada
pos = int(input("Mostrará la serie de Fibonacci hasta la posición: "))
for i in range(pos + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

#Prueba con valores del usuario
base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

#Asegurar que se muestre "0" si el número ingresado es 0
num = int(input("Ingrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(num)
print(f"Binario: {binario if binario else '0'}")


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#Ejemplo
print(es_palindromo("reconocer"))  #True
print(es_palindromo("python"))     #False



# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)



# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
