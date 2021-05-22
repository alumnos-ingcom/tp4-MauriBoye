################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Sexto ejercicio
"""
import tp4ej1

def minimo(lista):
    lista.sort()
    return lista[0]

def maximo(lista):
    lista.sort()
    lista.reverse()
    return lista[0]

def prueba():
    tp4ej1.marco("minimo()")
    lista = [7,2,8,1]
    minimo(lista)
    print(f"El menor numero de la lista es {minimo(lista)}")
    tp4ej1.marco("maximo()")
    maximo(lista)
    print(f"El mayor numero de la lista es {maximo(lista)}")

if __name__ == "__main__":
    prueba()