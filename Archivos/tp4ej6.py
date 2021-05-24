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

def lista_aleatoria(cantidad_numeros):
    nueva_lista_aleatoria=[]
    for i in range(cantidad_numeros):
        nueva_lista_aleatoria.append(random.randint(-100,100))
    return nueva_lista_aleatoria

def minimo(nueva_lista_aleatoria):
    """
    Esta función devuelve el menor numero de una lista
    """
    i=0
    menor=nueva_lista_aleatoria[i]
    while i < len(nueva_lista_aleatoria):
        if menor > nueva_lista_aleatoria[i]:
            menor=nueva_lista_aleatoria[i]
        i = i+1
    return menor

def maximo(nueva_lista_aleatoria):
    """
    Esta función devuelve el mayor numero de una lista
    """
    i=0
    mayor=nueva_lista_aleatoria[i]
    while i < len(nueva_lista_aleatoria):
        if mayor < nueva_lista_aleatoria[i]:
            mayor=nueva_lista_aleatoria[i]
        i = i+1
    return mayor

def prueba():
    nueva_lista_aleatoria = lista_aleatoria(tp4ej1.ingreso_numero("Ingrese la cantidad de numeros para la lista: "))
    tp4ej1.marco("minimo()")
    menor = minimo(nueva_lista_aleatoria)
    print(nueva_lista_aleatoria)
    print(f"El menor numero de la lista es {menor}")
    tp4ej1.marco("maximo()")
    mayor = maximo(nueva_lista_aleatoria)
    print(nueva_lista_aleatoria)
    print(f"El mayor numero de la lista es {mayor}")

if __name__ == "__main__":
    prueba()