from utils import es_numero_entero
def ordenar(vector=[]):
    orden = len(vector)
    for i in range(orden):
        for j in range(orden - 1):
            if vector[j] > vector[j+1]:
                temp = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = temp


def invitados():
    mayor_Edad=0
    menor_Edad=0
    cant_invitados = es_numero_entero(input("Digite la cantidad de invitados: \n"))
    edades=[]
    for i in range(cant_invitados):
        edad= es_numero_entero(input("Digite la edad del inivtado \n"))
        edades.append(edad)
    print("Las edades en desorden son: ")
    for edad in edades:
        print(edad)
    print(" ")
    print(" ")
    print("Las edades en orden son: ")
    ordenar(edades)
    for age in edades:
        print(age)
    print("....")
    for i in range(len(edades)):
        if edades[i]>=18:
            mayor_Edad+=1
        else:
            menor_Edad+=1
    print(f"Los mayores de edad son: {mayor_Edad}")
    print(f"Los menores de edad son: {menor_Edad}")

if __name__ == "__main__":
    invitados()