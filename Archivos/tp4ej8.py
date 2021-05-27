################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Octavo ejercicio
"""
import tp4ej1
import tp4ej6

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función devuelve una lista ordenada de mayor a menor
    """
    i=0
    lista=[uno,dos,tres]
    lista_mayor_a_menor = []
    while i < len(lista):
        lista_mayor_a_menor.append(tp4ej6.maximo(lista))
        lista.remove(tp4ej6.maximo(lista))
    return lista_mayor_a_menor
    
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función devuelve una lista ordenada de menor a mayor
    """
    i=0
    lista=[uno,dos,tres]
    lista_menor_a_mayor = []
    while i < len(lista):
        lista_menor_a_mayor.append(tp4ej6.minimo(lista))
        lista.remove(tp4ej6.minimo(lista))
    return lista_menor_a_mayor

def prueba():
    print("Orden de 3 numeros")
    numero1 = tp4ej1.ingreso_numero("Ingrese el 1er numero: ")
    numero2 = tp4ej1.ingreso_numero("Ingrese el 2do numero: ")
    numero3 = tp4ej1.ingreso_numero("Ingrese el 3er numero: ")
    tp4ej1.marco("ordenar_menor_a_mayor()")
    print(ordenar_menor_a_mayor(numero1,numero2,numero3))
    tp4ej1.marco("ordenar_mayor_a_menor()")
    print(ordenar_mayor_a_menor(numero1,numero2,numero3))
    
if __name__ == "__main__":
    prueba()