from utils import es_numero_entero
import random
def buscarNumero(vector,numero):
    for num in vector:
        if num == numero:
            return True
    return False
def adivinar_numero():
    intentos =3;
    g=0;
    tamaño=es_numero_entero(input("Digite el tamaño del vector\n"))
    vector=[random.randint(0,100) for i in range(tamaño)]
    print(" ")
    print("Tiene 3 intentos para adivinar el numero")
    for _ in range(intentos):
        numero = es_numero_entero(input("Digite un numero\n"))
        if (buscarNumero(vector, numero)):
            print("¡Felicidades!, el numero está en el vector")
            break
        else:
            print("Lo siento! el numero no está en el vector")
    else:
            print("¡lo siento, pero no adivinaste el numero!")
    for i in range(len(vector)):

        print(vector)
        break

if(__name__=="__main__"):
    adivinar_numero()