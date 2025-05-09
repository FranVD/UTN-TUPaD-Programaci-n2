#Práctico 5: Listas
#Franco Reynoso Arellano - C20

#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Crear una lista con cinco elementos y mostrar el penúltimo

clubes = ["Boca", "River", "San Lorenzo", "Independiente", "Racing"]
penultimo_club = clubes[-2]
print(penultimo_club)

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista

lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("como")
lista_vacia.append("estas?")
print(lista_vacia)

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso" 
print(animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7] #Define la lista de numeros
numeros.remove(max(numeros)) #Busca devolver el valor máximo de la lista, en este caso el 22, y lo elimina con el remove. 
print(numeros) #Imprime la lista de numeros, que ahora es [8, 15,3,7]

#Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar los dos primeros

numeros = list(range(10, 31, 5))
print(numeros[:2])  

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["golf", "chevy"]
print(autos)

#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Dada la lista “compras”, realizar las siguientes operaciones

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

#b Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

#c Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

#d Imprimir la lista resultante por pantalla
print(compras)


#Elaborar una lista anidada llamada “lista_anidada” con los siguientes elementos e imprimirla

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

