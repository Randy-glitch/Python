import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

#funcion de binarios
def Binario():
    if len(entry2.get())>0:
        entry2.delete(0, tk.END)
    
    b = entry.get()
    dec = int(str(b), 2)
    entry2.insert(0, dec )
    
def dele():
    entry2.delete(0, tk.END)
    entry.delete(0, tk.END)

#funcion de decimales
def  Decimal():
    if len(entry22.get())>0:
        entry22.delete(0, tk.END)
    n = int(entry20.get())

    binario= str((int(bin(n)[2:])))
    entry22.insert(0, binario )
def  Deletes():
    entry22.delete(0, tk.END)
    entry20.delete(0, tk.END)


root = tk.Tk()
root.config(width=250, height=260)
# label
label = ttk.Label(root, text='Binario - Decimal') 
label.place(x=50, y=25)


# Crear caja de texto.
entry = ttk.Entry(root)
entry2 = ttk.Entry(root)

# Posicionarla en la ventana.
entry.place(x=50, y=45)
entry2.place(x=50, y=65)

button1 = ttk.Button(root, text="ok",
    command = Binario)
button1.place(x=50, y=90)

button1 = ttk.Button(root, text="delete",
    command= dele )
button1.place(x=140, y=90)



label2 = ttk.Label(root, text='Decimal - Binario') 
label2.place(x=50, y=130)

# Crear caja de texto.
entry20 = ttk.Entry(root)
entry22 = ttk.Entry(root)

# Posicionarla en la ventana.
entry20.place(x=50, y=150)
entry22.place(x=50, y=170)

#buttons
button12 = ttk.Button(root, text="oks",
    command = Decimal)
button12.place(x=50, y=195)

button12 = ttk.Button(root, text="Borrar",
    command= Deletes )
button12.place(x=140, y=195)



root.mainloop()




