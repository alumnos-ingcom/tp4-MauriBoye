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
    return resultado

def prueba():
    tp4ej1.marco("suma_lenta()")
    print("Suma lenta de dos numeros")
    numero1=tp4ej1.ingreso_numero("Ingrese el 1er numero: ")
    numero2=tp4ej1.ingreso_numero("Ingrese el 2do numero: ")
    resultado=suma_lenta(numero1,numero2)
    print(f"({numero1})+({numero2})= {resultado}")

if __name__ == "__main__":
    prueba()
