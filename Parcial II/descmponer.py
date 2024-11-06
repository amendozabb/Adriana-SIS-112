def descomponer_numero(n):
    # Caso base: si n es menor que 10, devolver una lista con n
    if n < 10:
        return [n]
    # Caso recursivo: llamar a la función con n // 10 y agregar el último dígito n % 10
    else:
        return descomponer_numero(n // 10) + [n % 10]

# Solicitar al usuario que ingrese un número
n = int(input("Ingresa un número entero positivo: "))
if n < 0:
        print("Por favor, ingresa un número entero positivo.")
else:
        # Llamar a la función y mostrar el resultado
        resultado = descomponer_numero(n)
        print("Los dígitos del número son:", resultado)


