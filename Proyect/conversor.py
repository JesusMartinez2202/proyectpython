# Programa elaborado por Kevin Jesus Martinez Martinez

def Comprobacion(texto):
    if(texto == "" or texto == " "):
        print("\nIntroduce una frase")
        return texto
    else:
        return True

def Transform():
    text = input("Ingresa el texto a convertir: ")
    if( Comprobacion(text) == True ):
        text = text.upper()
        text2 = text.lower()
        print("Mayúsculas: ", text,
              "\nMinúsculas: ", text2)
    return 0
        
def Invert():
    inp = input("Ingresa el texto o números a invertir: ")
    if( Comprobacion(inp) == True ):
        inp2 = inp[::-1]
        print("Entrada original: ", inp,
            "\nEntrada invertida: ", inp2)
    return 0
    
def Palindrome():
    def palindromo(texto):
        texto = texto.replace(" ", "").lower()
        return texto == texto[::-1]
    
    entrada = input("Ingresa una palabra o frase: ")
    if( Comprobacion(entrada) == True ):
        if palindromo(entrada):
            print("Tu texto introducido SÍ es palíndromo")
        else:
            print("Tu texto introducido NO es palíndromo")
    return 0