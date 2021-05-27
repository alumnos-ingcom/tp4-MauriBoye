################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Decimo ejercicio
"""
import tp4ej1
import tp4ej9

def factores_primos(numero):
    """
    Esta funcion pide el ingreso de un numero y devuelve sus factores primos
    """
    i=1
    factor_primo=[1]
    while i <= numero:
        if tp4ej9.es_primo(i):
            if numero%i==0:
                factor_primo.append(i)
        i=i+1
    return tuple(factor_primo)

def prueba():
    tp4ej1.marco("factores_primos()")
    print("Factores primos")
    numero = tp4ej1.ingreso_numero("Ingrese un numero: ")
    print(f"Los factores primos de {numero} son {factores_primos(numero)}")

if __name__ == "__main__":
    prueba()