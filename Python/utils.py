def es_numero_entero(entrada):
    while True:
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Error: La entrada debe ser un número entero.")
            entrada = input("Por favor, ingrese un número entero: \n")
def es_numero_float(entrada):
    while True:
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Error: La entrada debe ser un numero decimal")
            entrada = input("Por favor, ingrese un numero decimal")


def es_palabra():
    while True:
        palabra = input("Ingresa una palabra: ")
        if isinstance(palabra, str):
            return palabra
        else:
            print("Error: Debes ingresar una palabra válida. Inténtalo nuevamente.")

