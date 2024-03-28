from utils import es_numero_entero
import random
from rich.console import Console
console = Console()
def dados(intentos=10):
    console.print("[bold magenta]Simulador de lanzamientos de dados[bold magenta]")
    console.print("[bold yellow]Tienes 10 intentos[bold yellow]")
    console.print("[bold green]1. lanzar los dados.\n 2. Dejarlos quietos[bold green]")
    op=es_numero_entero(console.input("[italic blue]Digita un numero\n[italic blue]"))
    if op==1:
        for i in range(intentos):
            dado_uno=random.randint(1,6)
            dado_dos=random.randint(1,6)
            vector_uno=[dado_uno]#Aqui se van a almacenar las jugadas del dado1
            vector_dos=[dado_dos]#Aqui lo mismo pero del dado 2
            console.print(f"[italic blue]Dado 1 : {dado_uno} || Dado 2 : {dado_dos}[italic blue]")
            if dado_uno==dado_dos:
                console.print(f"[italic green]Has sacado par ¡Ganado![italic green]")
            console.print(" ")
        console.print("[italic red]By: Daniel Sánchez[italic red]")
    elif op ==2:
        console.print(f"[code red]Has dejado quieto los dados[code red]")
    else:
        console.print(f"[bold red]Opción inválida ¡Adiós![bold red]")

if __name__=="__main__":
    dados()
