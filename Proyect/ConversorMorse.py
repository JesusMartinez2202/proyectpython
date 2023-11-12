# Definicion de funciones

# Funcion que convierte a Morse
def morse(texto):
    texto = texto.lower()
    texto = texto.replace("a", ".-")
    texto = texto.replace("á", ".-")
    texto = texto.replace("b", "-...")
    texto = texto.replace("c", "-.-.")
    texto = texto.replace("d", "-..")
    texto = texto.replace("e", ".")
    texto = texto.replace("é", ".")
    texto = texto.replace("f", "..-.")
    texto = texto.replace("g", "--.")
    texto = texto.replace("h", "....")
    texto = texto.replace("i", "..")
    texto = texto.replace("í", "..")
    texto = texto.replace("j", ".---")
    texto = texto.replace("k", "-.-")
    texto = texto.replace("l", ".-..")
    texto = texto.replace("m", "--")
    texto = texto.replace("n", "-.")
    texto = texto.replace("o", "---")
    texto = texto.replace("ó", "---")
    texto = texto.replace("p", ".--.")
    texto = texto.replace("q", "--.-")
    texto = texto.replace("r", ".-.")
    texto = texto.replace("s", "...")
    texto = texto.replace("t", "-")
    texto = texto.replace("u", "..-")
    texto = texto.replace("ú", "..-")
    texto = texto.replace("v", "...-")
    texto = texto.replace("w", ".--")
    texto = texto.replace("x", "-..-")
    texto = texto.replace("y", "-.--")
    texto = texto.replace("z", "--..")
    texto = texto.replace(" ", "/")
    return texto

# Arreglo que asigna a cada código su respectiva letra
morse_to_espanol = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
    "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
    "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
    ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
    "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
    "--..": "z", " ": " "
}

# Funcion que convierte de morse a español
def morse_a_espanol(texto):
    palabras = texto.split("  ")
    texto_espanol = []
    for palabra in palabras:
        caracteres = palabra.split(" ")
        for caracter in caracteres:
            texto_espanol.append(morse_to_espanol.get(caracter, ""))
        texto_espanol.append(" ")
    return "".join(texto_espanol)


# Funcion que comprueba que se haya introducido algo
def Comprobacion(texto):
    if(texto == ""):
        print("\n\tNo has introducido nada")
        return False
    else:
        return True

# Funcion que ejecuta el menu
def menu():
    while True:
        print("\n\t***** Submenú de Morse *****"
            "\n\t¿Qué quieres hacer?"
            "\n\t1. Convertir de español a morse"
            "\n\t2. Convertir de morse a español"
            "\n\t3. Salir")
        opcion = input("\n\tElige una opción: ")
        if(opcion == "1"):
            texto = input("\n\tIntroduce una frase: ")
            Comprobacion(texto)
            print("\n\t", morse(texto))
        elif(opcion == "2"):
            texto = input("\n\tIntroduce una frase (separa cada letra por un espacio): ")
            Comprobacion(texto)
            print("\n\t", morse_a_espanol(texto))
        elif(opcion == "3"):
            break
        else:
            print("\n\tOpción incorrecta")
    
        respuesta = input("\n\t¿Quieres hacer otra conversión? (s/n): ")
        if(respuesta.lower() != "s"):
            print("\n\tHasta pronto!!")
            break