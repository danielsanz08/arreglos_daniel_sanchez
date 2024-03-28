from rich.console import Console
console = Console()
from utils import es_numero_entero
def ordenar(vector=[]):
    orden = len(vector)
    for i in range(orden):
        for j in range(orden - 1):
            if vector[j] > vector[j+1]:
                temp = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = temp


def invitados():
    mayor_Edad=0
    menor_Edad=0
    cant_invitados = es_numero_entero(console.input("[bold green]Digite la cantidad de invitados: \n[bold green]"))
    edades=[]
    for i in range(cant_invitados):
        edad= es_numero_entero(console.input("[bold yellow]Digite la edad del inivtado \n"))
        edades.append(edad)
    console.print("[bold yellow]Las edades en desorden son: [bold yellow]")
    for edad in edades:
        print(edad)
    console.print(" ")
    console.print(" ")
    console.print("[italic green]Las edades en orden son: [italic green]")
    ordenar(edades)
    for age in edades:
        console.print(f"[italic red]{age}[italic red]")
    console.print("....")
    for i in range(len(edades)):
        if edades[i]>=18:
            mayor_Edad+=1
        else:
            menor_Edad+=1
    console.print(f"[code red]Los mayores de edad son: {mayor_Edad}[code red]")
    console.print(f"[code blue]Los menores de edad son: {menor_Edad}[code blue]")

if __name__ == "__main__":
    invitados()