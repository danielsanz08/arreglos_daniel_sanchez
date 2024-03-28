from utils import es_numero_entero
from utils import es_numero_float
from rich.console import Console
console = Console()
def compra():
    cant_compra=es_numero_entero(console.input("[bold blue]Ingrese la cantidad de productos a comprar\n[bold blue]"))
    precio_compra=[]
    precio_venta=[cant_compra]
    j=0
    k=0
    o=0

    while(j<cant_compra):
        producto= es_numero_float(console.input(f"[bold green]Digita el precio de la compra\n[bold green]"))
        precio_compra.append(producto)
        j+=1

    console.print(f"[italic yellow]Los precios son: [italic yellow]")
    while(k<len(precio_compra)):
        print(precio_compra[k])
        k+=1
    print(" ")
    console.print("[italic magenta]Las ventas mas el 10% es: [italic magenta]")
    while(o<len(precio_compra)):
        precio_venta= round(precio_compra[o]*1.1,2)
        console.print(f"[bold green]{precio_venta}[/bold green]")
        o+=1

if __name__ == "__main__":
    compra()