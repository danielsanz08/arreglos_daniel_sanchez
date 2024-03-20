from utils import es_numero_entero
from utils import es_numero_float

def asignar_valor(lista):
    for i in range(len(lista)):
        lista[i] = -1

def reemplazar_valor():
    ventas = [0] * 7
    asignar_valor(ventas)
    print("0. Lunes, 1. Martes, 2. Miércoles, 3.Jueves, 4. Viernes, 5. Sábado, 6. Domingo")
    dia = es_numero_entero(input("Digite el dia a registrar un valor\n"))
    for i in range(len(ventas)):
        valor = es_numero_float(input("Digite el valor\n"))
        print(" ")
        ventas[dia]=valor
        for venta in ventas:
            print(venta)
        break


if __name__ == "__main__":
    reemplazar_valor()
