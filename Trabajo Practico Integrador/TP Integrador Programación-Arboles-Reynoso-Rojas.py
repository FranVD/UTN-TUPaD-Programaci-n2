#TrabajoPracticoIntegrador #Programación
#ReynosoArellanoFranco // Rojas Máximiliano Yamil 

# Lista de 3 elementos: [nodo, subárbol_izquierdo, subárbol_derecho]
[7, [3, [1, None, None], [5, None, None]], [9, [8, None, None], [10, None, None]]]

# Insertar un valor en el árbol
def insertar(arbol, valor):
    if arbol is None:
        return [valor, None, None]  # Crea un nodo nuevo si el arbol está vacio
    if valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor) # Inserta en el subarbol izquierdo
    elif valor > arbol[0]:
        arbol[2] = insertar(arbol[2], valor) # Inserta en el subarbol derecho
    return arbol

# Busca un valor en el árbol
def buscar(arbol, valor):
    if arbol is None:   
        return False    # Si no se encontró devuelve false
    if valor == arbol[0]:  # Si se encontró devuelve true
        return True
    elif valor < arbol[0]:
        return buscar(arbol[1], valor) # Si no encontró busca en el subarbol izquierdo
    else:
        return buscar(arbol[2], valor) # # Si no encontró busca en subarbol derecho

# Imprime el árbol en orden
def imprimir_inorden(arbol):
    if arbol is not None:
        imprimir_inorden(arbol[1])  # hacia la izquierda
        print(arbol[0], end=' ')   # raíz
        imprimir_inorden(arbol[2])  # hacia la derecha


# Empieza el programa.

arbol = None

# Inserta los valores
for numero in [7, 3, 9, 1, 5, 8, 10]:
    arbol = insertar(arbol, numero)

# Imprime el árbol en orden
print("Valores en orden:")
imprimir_inorden(arbol)
print()

# Buscar un valor determinado
valor = 5
if buscar(arbol, valor):
    print(f"El valor {valor} está en el árbol.")
else:
    print(f"El valor {valor} NO está en el árbol.")

# Resultado esperado

# Valores en orden:
# 1 3 5 7 8 9 10 
# El valor 5 está en el árbol.



