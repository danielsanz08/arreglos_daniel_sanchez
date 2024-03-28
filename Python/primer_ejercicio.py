from rich.console import Console
console = Console()
import random
from utils import es_numero_entero
def menor_mayor(calificaciones):
    mayor =max(calificaciones)
    menor =min(calificaciones)
    return mayor,menor

def notas():
    cant_alumnos = es_numero_entero(console.input("[bold green]Digite la cantidad de los estudiantes\n[bold green]"))
    calificaciones = [random.randint(0, 100) for _ in range(cant_alumnos)]
    console.print(f"[bold yellow]Las calificaciones son: {calificaciones}[bold yellow]")

    menor = menor_mayor(calificaciones)
    mayor, menor = menor_mayor(calificaciones)
    console.print(f"[italic red]La nota mas baja es: {menor}[italic red] :disappointed_face:")
    console.print(f"[italic blue]La nota mas alta es: {mayor}[italic blue] :smiley:")

if __name__ == "__main__":
    notas()