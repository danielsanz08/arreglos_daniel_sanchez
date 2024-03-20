from utils import es_numero_entero
import random
def dados(intentos=10):
    print("Simulador de lanzamientos de dados")
    print("Tienes 10 intentos")
    print("1. lanzar los dados.\n 2. Dejarlos quietos")
    op=es_numero_entero(input("Digita un numero\n"))
    if op==1:
        for i in range(intentos):
            dado_uno=random.randint(1,6)
            dado_dos=random.randint(1,6)
            vector_uno=[dado_uno]#Aqui se van a almacenar las jugadas del dado1
            vector_dos=[dado_dos]#Aqui lo mismo pero del dado 2
            print(f"Dado 1 : {dado_uno} || Dado 2 : {dado_dos}")
            if dado_uno==dado_dos:
                print(f"Has sacado par ¡Ganado!")
            print(" ")
        print("By: Daniel Sánchez")
    elif op ==2:
        print(f"Has dejado quieto los dados")
    else:
        print(f"Opción inválida ¡Adiós!")

if __name__=="__main__":
    dados()
