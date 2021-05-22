################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Segundo ejercicio
"""
import tp4ej1

def suma_lenta(numero1,numero2):
    """
    Esta funcion pide el ingreso de 2 numeros para indicar la
    suma entre ellos sin hacer la operacion de manera directa.
    """
    try:
        contador=0
        resultado=numero1
        if numero2 > 0:
            while contador < numero2 :
                resultado = resultado + 1
                contador = contador + 1
        else:
            while contador > numero2 :
                resultado = resultado - 1
                contador = contador - 1
    except ValueError:
        raise tp4ej1.IngresoIncorrecto(f"Eso no es un número!")
    return resultado

def prueba():
    tp4ej1.marco("suma_lenta()")
    print("Suma lenta de dos numeros")
    numero1=3
    numero2=-5
    resultado=suma_lenta(numero1,numero2)
    print(f"({numero1})+({numero2})= {resultado}")

if __name__ == "__main__":
    prueba()
