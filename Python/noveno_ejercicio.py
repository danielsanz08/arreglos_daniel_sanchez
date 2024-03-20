from utils import es_numero_entero
import random
def buscar_numero(numero, vector):
    for num in vector:
        if num > numero:
            print("¡Frio, frio!")
            return True
        elif num < numero:
            print("¡Caliente, Caliente!")
            return
        else:
            print("¡Haz atinado!")
    print("El número no está en el vector.")

def main(intentos=5):
    i:0
    numeros=[0]*intentos
    aleatorio=[random.randint(0,100) for i in range(1)]
    print("Tienes 5 intentos para adivinar el número aleatorio")
    for i in range(intentos):
        num = es_numero_entero(input("digite un numero\n"))
        numeros[i] = num
        buscar_numero(num, aleatorio)
    if intentos==0:
        print("¡lo siento, pero no adivinaste!")
    print("El número a adivinar era: ")
    print(aleatorio)
    print("Los números que digitaste: ")
    for numero in numeros:
        print(numero)

if __name__=="__main__":
    main()