#Main

#Importación de archivos
from conversor import Transform, Invert, Palindrome
from ConversorMorse import menu
from Codificador import menu

opcion = int

print("\n***** BIENVENIDO AL TRATADOR DE CADENAS DE CARACTERES ****")

# Definición de funciones

#Funcion que ejecuta el menu
def Menu(opcion):
    opcion = input("\n1.- Transformar una cadena"
                   "\n2.- Invertir una cadena"
                   "\n3.- Decir si una cadena es palíndroma"
                   "\n4.- Conversor/Desconversor a Código Morse"
                   "\n5.- Encriptador/Desencriptador"
                   "\n6.- Salir"
                   "\nElige una opción: ")
    return opcion


#Funcion que comprueba que el valor introducido sea un numero entero
def Comprobacion(opcion):
    if( opcion.isdigit() == True ):
        return True
    else:
        return False

# Funcion que ejecuta opcion 1
def Transformar():
    Transform()

# Funcion que ejecuta opcion 2
def Invertir():
    Invert()

# Funcion que ejecuta opcion 3
def Palindromo():
    Palindrome()

# Funcion que ejecuta opcion 4
def Morse():
    menu()

# Funcion que ejecuta opcion 5
def Codificador():
    menu()

#Funcion que sale del programa
def Salir():
    print("\n***** GRACIAS POR UTILIZAR EL PROGRAMA *****")
    exit()

#Funcion que se ejecuta en caso de introducir algo invalido
def default():
    print("\nIntroduce una opción válida")


# Programa principal
while True:
    opcion = Menu(opcion)
    if( Comprobacion(opcion) == True ):

        switch = {
            "1": Transformar,
            "2": Invertir,
            "3": Palindromo,
            "4": Morse,
            "5": Codificador,
            "6": Salir
        }
        eleccion = opcion

        result = switch.get(eleccion, default)()
        print(result)

    else:
        print("¿Seguro que introdujiste un número?")
        continue

    respuesta = input("¿Deseas ejecutar otro programa? S/N: ")
    if( respuesta.lower() != "s"):
        print("\n***** GRACIAS POR UTILIZAR EL PROGRAMA *****")
        break