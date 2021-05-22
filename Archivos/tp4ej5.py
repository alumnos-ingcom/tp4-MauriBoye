################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Quinto ejercicio
"""
import tp4ej1

def signo(numero):
    """
    Esta funcion pide el ingreso de un numero e indica si es par o inpar
    """
    if numero==0:
        print(f"{numero} es cero")
    elif numero!=0 and numero%2==0:
        print(f"{numero} es par")
    elif numero!=0:
        print(f"{numero} es inpar")

def prueba():
    tp4ej1.marco("signo()")
    print ("Par, inpar o cero")
    signo(21)
    
if __name__ == "__main__":
    prueba()