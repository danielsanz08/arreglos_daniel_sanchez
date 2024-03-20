from utils import es_numero_entero
from utils import es_palabra
def eliminar_duplicados(vector=[]):
    for i in range(len(vector)):
        if vector[i] is not None:
            for j in range(i + 1, len(vector)):
                if vector[i] == vector[j]:
                    vector[j] = None
    return vector
def main(o=0):
    cant_nombres=es_numero_entero(input("Digita la cantidad de nombres de estudiantes que vas a digitar\n"))
    nombres=[cant_nombres]
    while o<cant_nombres:
        name = input("Digita los nombres, no importa si son iguales\n")
        nombres.append(name)
        o+=1
    print("Los nombres ingresados son:")
    for nombre in nombres:
        print(nombre)
    print(" ")
    no_duplicados=eliminar_duplicados(nombres)
    for i in range(len(no_duplicados)):
        if no_duplicados[i]!=None:
            print(no_duplicados[i])


if __name__=="__main__":
    main()