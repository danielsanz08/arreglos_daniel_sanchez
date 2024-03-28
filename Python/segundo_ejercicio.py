from utils import es_numero_entero
from utils import es_numero_float

from rich.console import Console
console = Console()
def asignar_valor(lista):
    for i in range(len(lista)):
        lista[i] = -1

def reemplazar_valor():
    ventas = [0] * 7
    asignar_valor(ventas)
    console.print("[italic blue]0. Lunes, 1. Martes, 2. Miércoles, 3.Jueves, 4. Viernes, 5. Sábado, 6. Domingo[italic blue]")
    dia = es_numero_entero(console.input("[bold yellow]Digite el dia a registrar un valor\n[bold yellow]"))
    for i in range(len(ventas)):
        valor = es_numero_float(console.input("[bold green]Digite el valor\n[bold green]"))
        print(" ")
        ventas[dia]=valor
        for venta in ventas:
            console.print(f"[code green]{venta}[code green]")
        break


if __name__ == "__main__":
    reemplazar_valor()
