def main():
  print("Hello learners!")

import tkinter as tk
from tkinter import messagebox


##Funcion 1 esta suma todos los números de una lista

def addmultiplenumbers(lista):
    if not lista:
        return 0
    return sum(lista)
#Funcion 2 multiplica todos los números de una lista
def multiplymultiplenumbers(lista):
    if not lista:
        return 0
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado
#Funcion 3 verificara si un número es par
def isiteven(numero):
    if not isitaninteger(numero):
        return False
    return numero % 2 == 0
#Funcion 4 verificara si un número es entero
def isitaninteger(numero):
    return isinstance(numero, int) or (isinstance(numero, float) and numero.is_integer())


#Funciones de la interfaz que dara a elegir la opcion que el usuario quiere realizar

def sumar():
    try:
        lista = [float(n) for n in entry_numeros.get().split(",")]
        resultado = addmultiplenumbers(lista)
        messagebox.showinfo("Resultado", f"La suma es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números separados por coma.")

def multiplicar():
    try:
        lista = [float(n) for n in entry_numeros.get().split(",")]
        resultado = multiplymultiplenumbers(lista)
        messagebox.showinfo("Resultado", f"El producto es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números separados por coma.")

def verificar_par():
    try:
        numero = float(entry_numero.get())
        resultado = isiteven(numero)
        messagebox.showinfo("Resultado", f"¿Es par?: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

def verificar_entero():
    try:
        numero = float(entry_numero.get())
        resultado = isitaninteger(numero)
        messagebox.showinfo("Resultado", f"¿Es entero?: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")


#Funcion para la interfaz gráfica

def main():
    global entry_numeros, entry_numero

    ventana = tk.Tk()
    ventana.title("Calculadora Interactiva")
    ventana.geometry("350x350")
    ventana.config(bg="#f0f0f0")

    #Etiqueta y entrada para suma y multiplicación
    tk.Label(ventana, text="Números (separados por coma):", bg="#f0f0f0").pack(pady=5)
    entry_numeros = tk.Entry(ventana, width=30)
    entry_numeros.pack(pady=5)

    #Se crean los botones de operaciones para las listas
    tk.Button(ventana, text="Sumar", command=sumar, width=15, bg="#4caf50", fg="white").pack(pady=5)
    tk.Button(ventana, text="Multiplicar", command=multiplicar, width=15, bg="#2196f3", fg="white").pack(pady=5)

    #Etiqueta y entrada para verificar
    tk.Label(ventana, text="Número individual:", bg="#f0f0f0").pack(pady=10)
    entry_numero = tk.Entry(ventana, width=30)
    entry_numero.pack(pady=5)

    #Se crean los botones de verificar
    tk.Button(ventana, text="¿Es par?", command=verificar_par, width=15, bg="#ff9800", fg="white").pack(pady=5)
    tk.Button(ventana, text="¿Es entero?", command=verificar_entero, width=15, bg="#9c27b0", fg="white").pack(pady=5)

    #Se crea el boton salir
    tk.Button(ventana, text="Salir", command=ventana.quit, width=15, bg="#f44336", fg="white").pack(pady=15)

    ventana.mainloop()

if __name__ == "__main__":
    main()
