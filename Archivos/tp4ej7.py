################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Septimo ejercicio
"""
import tp4ej1

def division_lenta(dividendo, divisor):
    """
    Esta funcion pide el ingreso de un dividendo y un divisor,
    luego devuelve el cociente y el resto de esa division.
    """
    resto=dividendo
    cociente=0
    while resto >= divisor:
        resto = resto-divisor
        cociente = cociente + 1
    lista = [cociente,resto]
    return lista

def prueba():
    tp4ej1.marco("division_lenta()")
    print("Resta sucesiva\n")
    dividendo = tp4ej1.ingreso_numero("Ingrese el dividendo: ")
    divisor = tp4ej1.ingreso_numero("Ingrese el divisor: ")
    cociente, resto = division_lenta(dividendo,divisor)
    print(f"{dividendo}/{divisor}= {cociente}\n"
          f"Resto= {resto}")

if __name__ == "__main__":
    prueba()
