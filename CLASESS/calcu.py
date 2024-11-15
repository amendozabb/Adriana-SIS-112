import tkinter as tk

# Ventana principal
root = tk.Tk()
root.title("Calculadora")

# Almacenar la expresión matemática
expression = ""

# Actualizar la expresión
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Evaluar la expresión
def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")


equation = tk.StringVar()

# Mostrar la expresión y el resultado
entry_field = tk.Entry(root, textvariable=equation, font=('Arial', 18), bd=8, insertwidth=2, width=14, borderwidth=4)
entry_field.grid(columnspan=4)

# Botones
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in button_texts:
    if text == '=':
        tk.Button(root, text=text, height=2, width=7, command=equalpress).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, height=2, width=7, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, height=2, width=7, command=lambda t=text: press(t)).grid(row=row, column=col)

root.mainloop()




