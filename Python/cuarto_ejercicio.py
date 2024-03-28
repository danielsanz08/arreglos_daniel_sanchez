from utils import es_numero_entero
import random
from rich.console import Console

console = Console()

def buscarNumero(vector, numero):
    for i in range(len(vector)):
        if vector[i] == numero:
            return i
    return -1

def adivinar_numero():
    intentos = 3
    tamaño = es_numero_entero(console.input("[bold blue]Digite el tamaño del vector\n[bold blue]"))
    vector = [random.randint(0, 101) for i in range(tamaño)]
    console.print(" ")
    console.print("[bold yellow]Tiene 3 intentos para adivinar el número[bold yellow]")
    for _ in range(intentos):
        numero = es_numero_entero(console.input("[bold magenta]Digite un número\n[bold magenta]"))
        indice = buscarNumero(vector, numero)
        if indice != -1:
            console.print(f"[italic green]¡Felicidades!, el número está en el índice {indice}[italic green]")
            break
        else:
            console.print("[italic red]Lo siento! el número no está en el vector[italic red]")
    else:
        console.print("[italic gray]¡Lo siento, pero no adivinaste el número![italic gray]")
    console.print(f"[bold blue]El vector es: {vector}")

if __name__ == "__main__":
    adivinar_numero()
