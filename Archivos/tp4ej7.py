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
    dividendo = 28
    divisor = 7
    tp4ej1.marco("division_lenta()")
    print("Resta sucesiva\n")
    lista = division_lenta(dividendo,divisor)
    print(f"{dividendo}/{divisor}= {lista[0]}\n"
          f"Resto= {lista[1]}")

if __name__ == "__main__":
    prueba()
