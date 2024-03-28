import random
from utils import es_numero_entero
from rich.console import Console
console = Console()
def calcular_frecuencia(letras=[]):
    frecuencia=[0]*26
    for letra in letras:
        frecuencia[ord(letra) - ord('a')] +=1
    console.print("[bold blue]La frecuencia de cada caracter: [bold blue]")
    for i in range(len(frecuencia)):
        console.print(f"[bold red]{chr(ord('a') + i)+": "+str(frecuencia[i])}[bold red]")

def cant_letras():
    letras = []
    cantidad = es_numero_entero(console.input("[italic magenta]Ingrese la cantidad de letras \n[italic magenta]"))
    for i in range(cantidad):
        letra = chr(ord('a') + int(random.random() * (ord('z') - ord('a') + 1)))
        letras.append(letra)

    console.print("[italic green]El vector es: [italic green]")
    for letra in letras:
        print(letra)
    console.print("[italic yellow]\nFrecuencia de letras:  [italic yellow]")
    calcular_frecuencia(letras)

if __name__ == "__main__":
    cant_letras()
