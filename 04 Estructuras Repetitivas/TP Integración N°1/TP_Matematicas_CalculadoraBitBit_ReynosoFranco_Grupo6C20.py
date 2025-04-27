#Trabajo Práctico Matematicas-Programación- Semana de Integración
#Programa: Calculadora de Operaciones Bit a Bit utilizando Python. 
#Autores: Franco Reynoso Arellano - Ignacio Robles - Santiago Rodriguez - Maximiliano Rojas - Héctor Romero
#Grupo 6 - Comisión 20


def mostrar_resultado(nombre_operacion, resultado, bit_resultado):
    # Imprime el nombre de la operación como encabezado
    print(f"{nombre_operacion}:")
    # Muestra el resultado en forma decimal (ej. 5)
    print(f"  Decimal: {resultado}")
    # Muestra el resultado en binario (ej. 0b101)
    print(f"  Binario: {bit_resultado}")
    print()  # Imprime una línea en blanco para separar visualmente los resultados

# Función principal que contiene la lógica del programa

def main():
    print("=== Calculadora de Operaciones Bit a Bit ===")

    try:
        # Solicita al usuario que ingrese el primer número
        num1 = int(input("Ingrese el primer número entero: "))
        # Solicita el segundo número entero de la misma manera
        num2 = int(input("Ingrese el segundo número entero: "))

        # --- OPERACIONES BIT A BIT ---
        resultado_and = num1 & num2
        resultado_or = num1 | num2
        resultado_xor = num1 ^ num2

        # Imprime un encabezado para los resultados
        print("\n--- Resultados ---")

        # Muestra los resultados de las operaciones
        mostrar_resultado("AND", resultado_and, bin(resultado_and))
        mostrar_resultado("OR", resultado_or, bin(resultado_or))
        mostrar_resultado("XOR", resultado_xor, bin(resultado_xor))

    except ValueError:
        print("Error: Por favor, ingrese solo números enteros.")


# Esta línea es un estándar para ejecutar el script directamente
if __name__ == "__main__":
    main()


