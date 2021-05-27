################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Cuarto ejercicio
"""
import tp4ej1

def comparacion(numero1,numero2):
    """
    Esta funcion pide el ingreso dos numeros y los compara
    """
    if numero1 < numero2:
        return -1
    elif numero1 == numero2:
        return 0
    elif numero1 > numero2:
        return 1

def prueba():
    tp4ej1.marco("comparacion()")
    print("Comparación entre 2 números")
    numero1 = tp4ej1.ingreso_numero("Ingrese el 1er numero: ")
    numero2 = tp4ej1.ingreso_numero("Ingrese el 2do numero: ")
    resultado = comparacion(numero1,numero2)
    if resultado == -1:
        print (f"{numero1} es menor que {numero2}")
    if resultado == 0:
        print (f"{numero1} es igual que {numero2}")
    if resultado == 1:
        print (f"{numero1} es mayor que {numero2}")

if __name__ == "__main__":
    prueba()