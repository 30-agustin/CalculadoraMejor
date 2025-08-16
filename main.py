
 #Funcion 1 esta suma todos los números de una lista
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

#Función principal que dara a elegir la opcion que el usuario quiere realizar
def main():
    print("¡Bienvenido a la calculadora!")
    
    while True:  # Bucle para repetir operaciones
        print("\nOpciones:")
        print("1) Sumar lista de números")
        print("2) Multiplicar lista de números")
        print("3) Verifica si un número es par")
        print("4) Verifica si un número es entero")
        print("5) Salir")
        
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        # Operaciones con listas para la suma y multiplicacion de numeros
        elif opcion in ["1", "2"]:
            numeros = input("Ingresa los números separados por coma: ")
            try:
                lista = [float(n) for n in numeros.split(",")]
                if opcion == "1":
                    print("Resultado:", addmultiplenumbers(lista))
                else:
                    print("Resultado:", multiplymultiplenumbers(lista))
            except ValueError:
                print("Error: Debes ingresar solo números separados por comas.")

        # Operaciones con un solo número para indicar si es par o entero
        elif opcion in ["3", "4"]:
            numero_input = input("Ingresa un número: ")
            try:
                numero = float(numero_input)
                if opcion == "3":
                    print("¿Es par?", isiteven(numero))
                else:
                    print("¿Es entero?", isitaninteger(numero))
            except ValueError:
                print("Error: Debes ingresar un número válido.")

        else:
            print("Opción no válida. Por favor, elige un número entre 1 y 5.")

# Ejecutar la calculadora
if __name__ == "__main__":
    main()
