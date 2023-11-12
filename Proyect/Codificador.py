import cryptocode 

# Definimos las funciones

# Funcion que comprueba que se introduzca algo en la frase
def Comprobacion(frase):
    if(frase == "" or frase == " "):
        print("\n\tIntroduce una frase")
        return frase
    else:
        return True

# Funcion que comprueba que se introduzca algo en la contraseña
def ComprobPass(password):
    
    if(password == "" or password == " "):
        print("\n\tIntroduce una contraseña")
        return False
    else:
        return True

#Funcion que ejecuta el menu
def menu():
    while True:
        eleccion = input("\n\t***** Submenú codificador de frases *****"
                        "\n\t¿Qué quieres hacer?"
                        "\n\t1. Codificar"
                        "\n\t2. Decodificar"
                        "\n\t3. Salir"
                        "\n\tElige una opción: ")
        if( eleccion == "1"):
            frase = input("\n\tIntroduce una frase: ")
            if( Comprobacion(frase) == True ):
                password = input("\n\tIntroduce una contraseña: ")
                if( ComprobPass(password) == True ):
                    print("\n\tLa frase codificada es: ", cryptocode.encrypt(frase, password))
        elif( eleccion == "2"):
            frase = input("\n\tIntroduce una frase: ")
            if( Comprobacion(frase) == True ):
                password = input("\n\tIntroduce una contraseña: ")
                if( ComprobPass(password) == True ):
                    if( cryptocode.decrypt(frase, password) == False ):
                        print("\n\tContraseña incorrecta")
                    else:
                        print("\n\tLa frase decodificada es: ", cryptocode.decrypt(frase, password))
        elif( eleccion == "3"):
            print("\n\t***** Gracias por utilizar el codificador de frases *****")
            break
        else:
            print("\n\tIntroduce una opción válida")
            continue