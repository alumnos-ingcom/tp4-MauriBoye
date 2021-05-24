################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Noveno ejercicio
"""
import tp4ej1

def es_primo(numero):
    """
    Esta funcion pide el ingreso de un numero y devuelve True si es primo
    """
    divisores=0
    i=1
    while i <= numero:
        if numero%i==0:
            divisores = divisores + 1
        i=i+1
    if divisores==2:
        return True
    else:
        return False
    
def prueba():
    tp4ej1.marco("es_primo()")
    print("Numeros primos")
    numero = tp4ej1.ingreso_numero("Ingrese un numero: ")
    if es_primo(numero):
        print(f"{numero} es un numero primo")
    else:
        print(f"{numero} no es un numero primo")

if __name__ == "__main__":
    prueba()
