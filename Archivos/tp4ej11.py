################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Decimo primer ejercicio
"""
import tp4ej1

def es_palindromo(texto):
    """
    Esta funcion pide el ingreso de una palabra o frase, e indica
    si es un palindromo.
    """
    a=0
    b=-1
    palindromo=[]
    palabra=[]
    while a<len(texto):
        if texto[a]!=" ":
            palabra.append(texto[a])
        if texto[b]!=" ":
            palindromo.append(texto[b])
        a=a+1
        b=b-1
    if palabra==palindromo:
        return True
            
def prueba():
    tp4ej1.marco("es_palindromo()")
    print("Palíndromo")
    texto= input("Ingrese una palabra o frase: ")
    if es_palindromo(texto):
        print(f"'{texto}' es palindromo")
    else:
        print(f"'{texto}' no es palindromo")

if __name__ == "__main__":
    prueba()