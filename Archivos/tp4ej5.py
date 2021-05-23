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
        return 0
    elif numero!=0 and numero%2==0:
        return 2
    elif numero!=0:
        return 1

def prueba():
    tp4ej1.marco("signo()")
    print ("Par, inpar o cero")
    numero = tp4ej1.ingreso_numero("Ingrese un numero: ")
    valor = signo(numero)
    if valor == 0:
        print(f"{numero} es cero")
    elif valor == 1:
        print(f"{numero} es inpar")
    elif valor == 2:
        print(f"{numero} es par")
    
if __name__ == "__main__":
    prueba()