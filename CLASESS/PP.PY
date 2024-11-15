import tkinter as tk
from tkinter import StringVar, ttk

root = tk.Tk()
root.title("Calculadora")
root.geometry("+500,80")

mainframe = ttk.frame(root)
mainframe.grid (column=0, row=0)

entrada1= StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1)
label_entrada1.grid (column=0, row=0)

entrada2= StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2)

button0 = ttk.Button(mainframe, text="0")
button1 = ttk.Button(mainframe, text="1")
button2 = ttk.Button(mainframe, text="2")
button3 = ttk.Button(mainframe, text="3")
button4 = ttk.Button(mainframe, text="4")
button5 = ttk.Button(mainframe, text="5")
button6 = ttk.Button(mainframe, text="6")
button7 = ttk.Button(mainframe, text="7")
button8 = ttk.Button(mainframe, text="8")
button9 = ttk.Button(mainframe, text="9")

button_borrar = ttk.Button(mainframe, text= chr=(9003))

root.mainloop()
