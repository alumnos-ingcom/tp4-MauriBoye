################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Primer ejercicio
"""

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_numero(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero.
    """
    ingreso=input(mensaje)
    try:
        entero=int(ingreso)
        print("Todo bien master")
    except ValueError as err:
        raise IngresoIncorrecto(f"'{ingreso}' no es un número!") from err
    return entero    

def ingreso_numero_limite(mensaje,minimo=0,maximo=10):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero entre dos valores limites.
    """
    print(mensaje)
    print(f"Minimo: {minimo}")
    print(f"Maximo: {maximo}")
    entero=ingreso_numero("Ingrese un numero: ")
    if entero < minimo or entero > maximo:
        raise IngresoIncorrecto(f"'{entero}' no esta dentro del rango!")
    return entero

def ingreso_numero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero con una determinada cantidad de reintentos.
    """
    intentos= cantidad_reintentos
    while intentos>0:
        try:
            return ingreso_numero(mensaje)
        except IngresoIncorrecto:
            intentos = intentos - 1
            print(f"Valor incorrecto, le queda {intentos} intentos \n")
    raise IngresoIncorrecto("Se acabaron los intentos disponibles")
        
def prueba():
    print ("-----------------------------------------------------------------------------------")
    print ("ingreso_numero()")
    print ("-----------------------------------------------------------------------------------")
    ingreso_numero("Ingrese un numero: ")
    print ("\n-----------------------------------------------------------------------------------")
    print ("ingreso_numero_limite()")
    print ("-----------------------------------------------------------------------------------")
    ingreso_numero_limite("Ingrese un numero entero entre los valores límites")
    print ("\n-----------------------------------------------------------------------------------")
    print ("ingreso_numero_reintento()")
    print ("-----------------------------------------------------------------------------------")
    ingreso_numero_reintento("Ingrese un numero: ")

if __name__ == "__main__":
    prueba()
