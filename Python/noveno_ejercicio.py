from utils import es_numero_entero
from rich.console import Console
console = Console()
import random
def buscar_numero(numero, vector):
    for num in vector:
        if num > numero:
            console.print("[italic blue]¡Frio, frio![italic blue]")
            return True
        elif num < numero:
            console.print("[italic red]¡Caliente, Caliente![italic red]")
            return
        else:
            console.print("[italic green]¡Haz atinado![italic green]")
    console.print("[bold red]El número no está en el vector.[bold red]")

def main(intentos=5):
    i:0
    numeros=[0]*intentos
    aleatorio=[random.randint(0,100) for i in range(1)]
    console.print("[bold magenta]Tienes 5 intentos para adivinar el número aleatorio[bold magenta]")
    for i in range(intentos):
        num = es_numero_entero(console.input("[bold magenta]digite un numero\n[bold magenta]"))
        numeros[i] = num
        buscar_numero(num, aleatorio)
    if intentos==0:
        console.print("[italic red]¡lo siento, pero no adivinaste![italic red]")
    console.print("[italic green]El número a adivinar era: [italic green]")
    console.print(f"[italic blue]{aleatorio}[italic blue]")
    console.print("[bold yellow]Los números que digitaste: [bold yellow]")
    for numero in numeros:
        console.print(f"{numero}")

if __name__=="__main__":
    main()