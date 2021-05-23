################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Sexto ejercicio
"""
import tp4ej1
import random

def lista(cantidad_numeros):
    nueva_lista=[]
    for i in range(cantidad_numeros):
        nueva_lista.append(random.randint(-100,100))
    return nueva_lista

def minimo(nueva_lista):
    """
    Esta función devuelve el menor numero de una lista
    """
    i=0
    menor=nueva_lista[i]
    while i < len(nueva_lista):
        if menor > nueva_lista[i]:
            menor=nueva_lista[i]
        i = i+1
    return menor

def maximo(nueva_lista):
    """
    Esta función devuelve el mayor numero de una lista
    """
    i=0
    mayor=nueva_lista[i]
    while i < len(nueva_lista):
        if mayor < nueva_lista[i]:
            mayor=nueva_lista[i]
        i = i+1
    return mayor

def prueba():
    nueva_lista = lista(tp4ej1.ingreso_numero("Ingrese la cantidad de numeros para la lista: "))
    tp4ej1.marco("minimo()")
    menor = minimo(nueva_lista)
    print(nueva_lista)
    print(f"El menor numero de la lista es {menor}")
    tp4ej1.marco("maximo()")
    mayor = maximo(nueva_lista)
    print(nueva_lista)
    print(f"El mayor numero de la lista es {mayor}")

if __name__ == "__main__":
    prueba()