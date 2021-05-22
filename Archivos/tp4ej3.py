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
    try:
        fahrrenheit = (centigrados * 9/5) + 32
    except ValueError:
        raise tp4ej1.IngresoIncorrecto(f"'{centigrados}' no es un número!")
    return fahrrenheit

def convertir_a_centigrados(fahrrenheit):
    """
    Esta funcion pide el ingreso de una temperatura en fahrrenheit
    para indicar la conversion a centigrados.
    """
    try:
        centigrados = (fahrrenheit - 32) * 5/9
    except ValueError:
        raise tp4ej1.IngresoIncorrecto(f"'{fahrrenheit}' no es un número!")
    return centigrados

def prueba():
    tp4ej1.marco("convertir_a_fahrrenheit()")
    print ("Conversion de centigrados a fahrrenheit")
    centigrados = 24
    fahrrenheit = convertir_a_fahrrenheit(centigrados)
    print (f"{centigrados}°C son {fahrrenheit}°F")
    tp4ej1.marco("convertir_a_centigrados()")
    print ("Conversion de fahrrenheit a centigrados")
    fahrrenheit = 75.2
    centigrados = convertir_a_centigrados(fahrrenheit)
    print (f"{fahrrenheit}°F son {centigrados}°C")

if __name__ == "__main__":
    prueba()
