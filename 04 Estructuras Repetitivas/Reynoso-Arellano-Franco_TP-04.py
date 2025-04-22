#Práctico 4: Estructuras repetitivas 
#Franco Reynoso Arellano 

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100, incluyendo ambos extremos, en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingrese un número entero: ")
print("Cantidad de dígitos:", len(numero))

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

inicio = min(num1, num2) + 1 #Con esto excluyo el numero minimo extremo
fin = max(num1, num2) #El mayor no es necesario ya que el fin lo excluye por si mismo

suma = 0
for i in range(inicio, fin):
    suma += i

print("La suma de los números entre", num1, "y", num2, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

total = 0
while True:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    if numero == 0:
        break
    total += numero

print("La suma total es:", total)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_secreto = random.randint(0, 9)
cantidad_de_intentos = 0

while True:
    cantidad_de_intentos = int(input("Adiviná el número (0 a 9): "))
    cantidad_de_intentos += 1
    if cantidad_de_intentos == numero_secreto:
        print("¡Correcto! Lo lograste en ", cantidad_de_intentos, "intentos.")
        break
    else:
        print("Incorrecto, seguí participando!.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

n = 100 
while n >= 0:
    print(n)
    n -= 2 #con esto resto de 2 en 2 hasta llegar a cero

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma desde 0 hasta", n, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = impares = positivos = negativos = 0
cantidad = 100

for _ in range(cantidad):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0: #si es divisible por 2, es par
        pares += 1 #lo uso para contar cuantas veces ocurre, o sea cada par se suma 1 al contador (aplica la misma logica al impar, positivos, negativos)
    else:
        impares += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

suma = 0
cantidad = 4

for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    suma += numero

media = suma / cantidad
print("La media de los números dados es de:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número: ")
invertido = numero[::-1] #esto invierte lo ingresado por el usuario
print("Número invertido:", invertido)
