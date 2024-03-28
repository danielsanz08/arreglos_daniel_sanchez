from utils import es_numero_entero
from rich.console import Console
console = Console()
def calcular_promedio(Lunes=[], Viernes=[]):
    cant_temperatura = len(Lunes)
    vector_nuevo = []
    for i in range(cant_temperatura):
        vector_nuevo.append((Lunes[i] + Viernes[i]) / 2)
    return vector_nuevo

def tomaTemperatura():
    dia= ["Lunes","Viernes"]
    cant_temperatura =es_numero_entero(console.input("[bold blue]Digita la cantidad de veces que deseen realizar la toma de temperatura por dia\n[bold blue]"))
    lunes=[]
    viernes=[]
    console.print("[code green]Toma de temperatura del dia Lunes[code green]")
    for i in range(cant_temperatura):
        temp_lun=es_numero_entero(console.input(f"[bold yellow]Digita la temperatura {i+1} \n[bold yellow]"))
        lunes.append(temp_lun)
    console.print("[code magenta]Toma de temperatura del dia Viernes[code magenta]")
    for i in range(cant_temperatura):
        temp_viernes=es_numero_entero(console.input(f"[bold blue]Digita la temperatura {i+1} \n[bold blue]"))
        viernes.append(temp_viernes)
    nuevo_vector= calcular_promedio(lunes, viernes)
    console.print("[italic blue]promedio de las temperaturas de Lunes y Viernes:[italic blue]")
    for i in range(len(dia)):
        console.print(f"[italic blue]Promedio del dia {dia[i]} : {nuevo_vector[i]} °C [italic blue]")




if __name__ == "__main__":
    tomaTemperatura()