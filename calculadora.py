def calculadora():
    operacion = input("Ingresa la operación deseada (+, -, *, /): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == '+':
        resul = num1 + num2
    elif operacion == '-':
        resul = num1 - num2
    elif operacion == '*':
        resul = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            resul = "Error: No se puede dividir por cero."
        else:
            resul = num1 / num2
    else:
        resul = "Operación no válida. Usa +, -, * o /."

    print(f"El resultado es: {result}")

if __name__ == "__main__":
    calculator()


