from rich.console import Console
console = Console()

def es_numero_entero(entrada):
    while True:
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            console.print("[italic red]Error: La entrada debe ser un número entero.[italic red]")
            entrada = console.input("[bold yellow]Por favor, ingrese un número entero: \n[bold yellow]")
def es_numero_float(entrada):
    while True:
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            console.print("[italic red]Error: La entrada debe ser un numero decimal[italic red]")
            entrada = console.input("[bold yellow]Por favor, ingrese un numero decimal[bold yellow]")


def es_palabra():
    while True:
        palabra = console.input("[italic green]Ingresa una palabra: [italic green]")
        if isinstance(palabra, str):
            return palabra
        else:
            console.print("[italic yellow]Error: Debes ingresar una palabra válida. Inténtalo nuevamente.[italic yellow]")

