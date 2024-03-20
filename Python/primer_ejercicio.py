import random
from utils import es_numero_entero
def menor_mayor(calificaciones):
    mayor =max(calificaciones)
    menor =min(calificaciones)
    return mayor,menor

def notas():
    cant_alumnos = es_numero_entero(input("Digite la cantidad de los estudiantes\n"))
    calificaciones = [random.randint(0, 100) for _ in range(cant_alumnos)]
    print(f"Las calificaciones son: {calificaciones}")

    menor = menor_mayor(calificaciones)
    mayor, menor = menor_mayor(calificaciones)
    print(f"La nota mas baja es: {menor}")
    print(f"La nota mas alta es: {mayor}")

if __name__ == "__main__":
    notas()