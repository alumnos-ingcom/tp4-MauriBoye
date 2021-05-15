################
# Mauricio Boyé - @MauriBoye
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_numero(mensaje):
    while True:
        ingreso=input(mensaje)
        try:
            entero=int(ingreso)
            if entero >= 0 or entero < 0:
                return entero
                break
        except ValueError:
            print(f"({ingreso}) no es un numero!")
            print("")
            
        

def ingreso_numero_limite():
    print("Ingrese los valores limites")
    minimo=ingreso_numero("Minimo: ")
    maximo=ingreso_numero("Maximo: ")
    while True:
        entero=ingreso_numero("Ingrese un numero: ")
        if entero > minimo and entero < maximo:
            print("Todo bien master")
            break
        else:
            print(f"({entero}) no esta dentro del rango")
            print("")
            continue



def prueba():
    ingreso_numero_limite()
    pass

if __name__ == "__main__":
    prueba()