import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Variable para almacenar la expresión
expression = ""

# Función para actualizar la expresión en la entrada de texto
def update_expression(value):
    global expression
    expression += str(value)
    input_text.set(expression)

# Función para evaluar la expresión y mostrar el resultado
def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))  # Evalúa la expresión
        input_text.set(result)         # Muestra el resultado en la entrada
        expression = result            # Actualiza la expresión con el resultado
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Función para borrar la entrada
def clear_expression():
    global expression
    expression = ""
    input_text.set("")

# Variable para la entrada de texto
input_text = tk.StringVar()

# Crear la entrada de texto
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right')
input_field.grid(row=0, column=0)
input_field.pack()

# Crear el marco para los botones
button_frame = tk.Frame(root)
button_frame.pack()

# Definir los botones
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', 'C', '=', '+'
]

# Crear y colocar los botones en la cuadrícula
row_value = 0
col_value = 0
for button in buttons:
    if button == "=":
        tk.Button(button_frame, text=button, font=('Arial', 18), fg='black', width=4, height=2, bd=1, command=evaluate_expression).grid(row=row_value, column=col_value)
    elif button == "C":
        tk.Button(button_frame, text=button, font=('Arial', 18), fg='black', width=4, height=2, bd=1, command=clear_expression).grid(row=row_value, column=col_value)
    else:
        tk.Button(button_frame, text=button, font=('Arial', 18), fg='black', width=4, height=2, bd=1, command=lambda x=button: update_expression(x)).grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Ejecutar el bucle de la aplicación
root.mainloop()
