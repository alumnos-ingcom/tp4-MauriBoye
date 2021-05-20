################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################################
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
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
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
    print(mensaje)
    print(f"Minimo: {minimo}")
    print(f"Maximo: {maximo}")
    while True:
        entero=ingreso_numero("Ingrese un numero: ")
        if entero > minimo and entero < maximo:
            break
        else:
            raise IngresoIncorrecto(f"'{entero}' no esta dentro del rango!")
        return entero

def ingreso_numero_reintento(mensaje, cantidad_reintentos=5):
    intentos= cantidad_reintentos
    while intentos>0:
        try:
            return ingreso_numero(mensaje)
        except IngresoIncorrecto:
            intentos-=1
            print(f"Valor incorrecto, le queda {intentos} intentos")
            print("")
    raise IngresoIncorrecto("Se acabaron los intentos disponibles")
        
def prueba():
    print ("-----------------------------------------------------------------------------------")
    print ("ingreso_numero()")
    print ("-----------------------------------------------------------------------------------")
    ingreso_numero("Ingrese un numero: ")
    print ("")
    print ("-----------------------------------------------------------------------------------")
    print ("ingreso_numero_limite()")
    print ("-----------------------------------------------------------------------------------")
    ingreso_numero_limite("Ingrese un numero entero entre los valores límites")
    print ("")
    print ("-----------------------------------------------------------------------------------")
    print ("ingreso_numero_reintento()")
    print ("-----------------------------------------------------------------------------------")
    ingreso_numero_reintento("Ingrese un numero: ")

if __name__ == "__main__":
    prueba()