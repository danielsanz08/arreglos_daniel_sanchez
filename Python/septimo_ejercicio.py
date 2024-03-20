import random
from utils import es_numero_entero
def calcular_frecuencia(letras=[]):
    frecuencia=[0]*26
    for letra in letras:
        frecuencia[ord(letra) - ord('a')] +=1
    print("La frecuencia de cada caracter: ")
    for i in range(len(frecuencia)):
        print(chr(ord('a') + i)+": "+str(frecuencia[i]))

def cant_letras():
    letras = []
    cantidad = es_numero_entero(input("Ingrese la cantidad de letras \n"))
    for i in range(cantidad):
        letra = chr(ord('a') + int(random.random() * (ord('z') - ord('a') + 1)))
        letras.append(letra)

    print("El vector es: ")
    for letra in letras:
        print(letra)
    print("\nFrecuencia de letras:  ")
    calcular_frecuencia(letras)

if __name__ == "__main__":
    cant_letras()
