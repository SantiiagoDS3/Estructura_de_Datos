# Inicializar listas para representar la cola y la pila
cola = []
pila = []

# Función para agregar un número a la cola
def agregar_a_cola(numero):
    if numero not in cola:
        cola.append(numero)
        print(f"Se ha agregado el número {numero} a la cola.")
    else:
        print(f"El número {numero} ya está en la cola.")

# Función para agregar un número a la pila
def agregar_a_pila(numero):
    if numero not in pila:
        pila.append(numero)
        print(f"Se ha agregado el número {numero} a la pila.")
    else:
        print(f"El número {numero} ya está en la pila.")

# Función para mostrar los elementos de la cola
def mostrar_cola():
    print("Elementos en la cola:")
    for elemento in cola:
        print(elemento, end=" ")
    print()

# Función para mostrar los elementos de la pila
def mostrar_pila():
    print("Elementos en la pila:")
    for elemento in reversed(pila):
        print(elemento, end=" ")
    print()

# Función principal
def main():
    while True:
        try:
            opcion = int(input("1. Agregar número a la cola\n2. Agregar número a la pila\n3. Mostrar cola\n4. Mostrar pila\n5. Salir\nSeleccione una opción: "))
            if opcion == 1:
                numero = int(input("Ingrese un número para la cola: "))
                agregar_a_cola(numero)
            elif opcion == 2:
                numero = int(input("Ingrese un número para la pila: "))
                agregar_a_pila(numero)
            elif opcion == 3:
                mostrar_cola()
            elif opcion == 4:
                mostrar_pila()
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    main()