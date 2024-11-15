import funciones  # Importa las funciones necesarias de funciones.py

def menu():
    # Inicializa dos listas, una para los datos ingresados manualmente y otra para los generados aleatoriamente
    lista_manual = []
    lista_aleatoria = []

    # Ciclo principal del menú
    while True:
        print("\nMenú Principal")
        print("1. Ingresar lista manualmente")
        print("2. Generar lista aleatoria")
        print("3. Ordenar lista")
        print("4. Búsqueda lineal")
        print("5. Búsqueda binaria")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        # Opción 1: Crear lista manualmente
        if opcion == "1":
            lista_manual = funciones.ingresar_lista()
             print(f"Lista manual creada: {lista_manual}")

        # Opción 2: Generar lista aleatoria de números únicos
        elif opcion == "2":
            n = int(input("Ingrese el tamaño de la lista aleatoria: "))
            lista_aleatoria = funciones.generar_lista_aleatoria(n)
            print(f"Lista aleatoria generada: {lista_aleatoria}")

        # Opción 3: Ordenar lista seleccionada por el usuario
        elif opcion == "3":
            lista = seleccionar_lista(lista_manual, lista_aleatoria)
            if lista == lista_manual:
                print("Ordenando lista manual...")
                funciones.ordenar_lista(lista_manual)
                print(f"Lista ordenada: {lista_manual}")
            elif lista == lista_aleatoria:
                print("Ordenando lista aleatoria...")
                funciones.ordenar_lista(lista_aleatoria)
                print(f"Lista ordenada: {lista_aleatoria}")

        # Opción 4: Realizar búsqueda lineal en la lista seleccionada
        elif opcion == "4":
            lista = seleccionar_lista(lista_manual, lista_aleatoria)
            numero = int(input("Ingrese el número a buscar: "))
            posicion = funciones.busqueda_lineal(lista, numero)
            mensaje_busqueda(posicion)
 # Opción 5: Realizar búsqueda binaria en la lista seleccionada
        elif opcion == "5":
            lista = seleccionar_lista(lista_manual, lista_aleatoria)
            # Verifica si la lista está ordenada antes de la búsqueda binaria
            if not funciones.esta_ordenada(lista):
                print("La lista no está ordenada. Ordenándola antes de la búsqueda binaria...")
                funciones.ordenar_lista(lista)
            numero = int(input("Ingrese el número a buscar: "))
            posicion = funciones.busqueda_binaria(lista, numero)
            mensaje_busqueda(posicion)

        # Opción 6: Salir del programa
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Función para elegir entre la lista manual y la lista aleatoria
def seleccionar_lista(lista_manual, lista_aleatoria):
    print("\nSeleccione la lista a utilizar:")
    print("1. Lista manual")
    print("2. Lista aleatoria")
    opcion = input("Seleccione una opción: ")
 if opcion == "1":
        return lista_manual
    elif opcion == "2":
        return lista_aleatoria
    else:
        print("Opción inválida. Usando lista manual por defecto.")
        return lista_manual

# Función para mostrar el resultado de la búsqueda de forma clara
def mensaje_busqueda(posicion):
    if posicion != -1:
        print(f"El número se encuentra en la posición {posicion}.")
    else:
        print("El número no se encontró en la lista.")

# Inicia el programa llamando a la función menu() si este archivo se ejecuta directamente
if name == "main":
    menu()

import random

def ingresar_lista():
    lista = []
    print("Ingrese números (deje vacío para terminar):")
    while True:
        num = input("Número: ")
        if num == "":
            break
        num = int(num)
        if num not in lista:
            lista.append(num)
    return lista

def generar_lista_aleatoria(n):
    return random.sample(range(1, n * 10), n)
def ordenar_lista(lista):
    # Ordenamiento por burbuja
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def busqueda_lineal(lista, numero):
    return lista.index(numero) if numero in lista else -1

def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


import random  # Importa la librería random para generar números aleatorios

# Función que permite al usuario ingresar números únicos en una lista manualmente
def ingresar_lista():
    lista = []
    print("Ingrese números (escriba 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':  # Permite al usuario terminar la entrada de números
            break
        try:
            numero = int(entrada)
            if numero not in lista:  # Verifica que el número no se repita
                lista.append(numero)
            else:
                print("El número ya está en la lista. Intente con otro.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
    return lista

# Función que genera una lista aleatoria de números únicos
def generar_lista_aleatoria(n):
    lista = []
  while len(lista) < n:
        numero = random.randint(1, 100)  # Genera un número entre 1 y 100
        if numero not in lista:  # Asegura que no haya números repetidos
            lista.append(numero)
    return lista

# Función que ordena una lista usando el método de burbuja
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:  # Intercambia los elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Función que realiza una búsqueda lineal en la lista
def busqueda_lineal(lista, numero):
    for i, valor in enumerate(lista):
        if valor == numero:  # Retorna la posición si el número es encontrado
            return i
    return -1  # Retorna -1 si el número no está en la lista

# Función que realiza una búsqueda binaria en una lista ordenada
def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:  # Retorna la posición si el número es encontrado
            return medio
