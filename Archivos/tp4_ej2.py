################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4_ej1 import ingreso_numero

def suma_lenta():
    print("Suma lenta de dos numeros")
    numero1=ingreso_numero("Ingrese el primer numero: ")
    numero2=ingreso_numero("Ingrese el segundo numero: ")
    contador=0
    resultado=numero1
    if numero2 > 0:
        while contador < numero2 :
            resultado += 1
            contador +=1
    else:
        while contador > numero2 :
            resultado -= 1
            contador -=1
    print(f"El resultado es: {resultado}")
    
def prueba():
    suma_lenta()
    pass

if __name__ == "__main__":
    prueba()