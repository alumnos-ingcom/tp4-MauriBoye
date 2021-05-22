################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
Tercer ejercicio
"""
import tp4ej1

def convertir_a_fahrrenheit(centigrados):
    """
    Esta funcion pide el ingreso de una temperatura en centigrados
    para indicar la conversion a fahrrenheit.
    """
    print ("Conversion de centigrados a fahrrenheit")
    try:
        centigrados = float(centigrados)
        fahrrenheit = (centigrados * 9/5) + 32
    except ValueError:
        raise tp4ej1.IngresoIncorrecto(f"'{centigrados}' no es un número!")
    print (f"{centigrados}°C son {fahrrenheit}°F")
    return fahrrenheit

def convertir_a_centigrados(fahrrenheit):
    """
    Esta funcion pide el ingreso de una temperatura en fahrrenheit
    para indicar la conversion a centigrados.
    """
    print ("Conversion de fahrrenheit a centigrados")
    try:
        fahrrenheit = float(fahrrenheit)
        centigrados = (fahrrenheit - 32) * 5/9
    except ValueError:
        raise tp4ej1.IngresoIncorrecto(f"'{fahrrenheit}' no es un número!")
    print (f"{fahrrenheit}°F son {centigrados}°C")
    return centigrados

def prueba():
    print ("-----------------------------------------------------------------------------------")
    print ("convertir_a_fahrrenheit()")
    print ("-----------------------------------------------------------------------------------")
    convertir_a_fahrrenheit(24)
    print ("")
    print ("-----------------------------------------------------------------------------------")
    print ("convertir_a_centigrados()")
    print ("-----------------------------------------------------------------------------------")
    convertir_a_centigrados(75.2)

if __name__ == "__main__":
    prueba()