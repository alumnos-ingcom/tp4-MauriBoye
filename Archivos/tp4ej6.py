################
# Mauricio Boyé - @MauriBoye
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

def minimo(lista):
    """
    Esta función devuelve el menor numero de una lista
    """
    i=0
    menor=lista[i]
    while i < len(lista):
        if menor > lista[i]:
            menor= lista[i]
        i = i+1
    return menor

def maximo(lista):
    """
    Esta función devuelve el mayor numero de una lista
    """
    i=0
    mayor=lista[i]
    while i < len(lista):
        if mayor < lista[i]:
            mayor= lista[i]
        i = i+1
    return mayor

def prueba():
    lista = lista_aleatoria(tp4ej1.ingreso_numero("Ingrese la cantidad de numeros para la lista: "))
    tp4ej1.marco("minimo()")
    menor = minimo(lista)
    print(lista)
    print(f"El menor numero de la lista es {menor}")
    tp4ej1.marco("maximo()")
    mayor = maximo(lista)
    print(lista)
    print(f"El mayor numero de la lista es {mayor}")

if __name__ == "__main__":
    prueba()