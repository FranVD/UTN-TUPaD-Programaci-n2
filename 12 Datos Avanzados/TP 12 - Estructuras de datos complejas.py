#TP 12: Estructuras de datos complejas
#Autor: Reynoso Arellano, Franco Gastón

#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 28000

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

lista_frutas = list(precios_frutas.keys())
print("Frutas disponibles:", lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}

print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá un nombre {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono

consulta = input("Ingresá el nombre de un contacto: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.lower().split()  
palabras_unicas = set(palabras)
print("\nPalabras únicas:", palabras_unicas)

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("\nFrecuencia de palabras:")
for palabra, cantidad in frecuencia_palabras.items():
    print(f"{palabra}: {cantidad}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {"Franco", "Maximiliano", "Santiago", "Lucila", "Ariadna"}
parcial2 = {"Franco", "Elias", "Pedro", "Lucila", "Ariadna"}
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe. 

stock_productos = {
    "Harina": 10,
    "Pan": 20,
    "Queso": 12
}

producto = input("Ingrese el nombre del producto: ")

if producto in stock_productos:
    print(f"El stock actual de {producto}: {stock_productos[producto]}")
    agregar = input("¿Querés agregar más unidades? (Si/No): ").lower()
    if agregar == "Si":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"{producto} no existe en el stock.")
    agregar_nuevo = input("¿Querés agregarlo? (Si/No): ").lower()
    if agregar_nuevo == "Si":
        cantidad = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} agregado con {cantidad} unidades.")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("Lunes", "08:00"): "Daily Sprint",
    ("Martes", "17:00"): "Gimnasio",
    ("Miércoles", "20:30"): "Clase Programación"
}

print("\nAgenda actual:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Perú": "Lima",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido (capital -> país):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")
