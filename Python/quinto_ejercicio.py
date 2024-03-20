from utils import es_numero_entero
from utils import es_numero_float
def compra():
    cant_compra=es_numero_entero(input("Ingrese la cantidad de productos a comprar\n"))
    precio_compra=[]
    precio_venta=[cant_compra]
    j=0
    k=0
    o=0
    i=0
    while(j<cant_compra):
        producto= es_numero_float(input(f"Digita el precio de la compra\n"))
        precio_compra.append(producto)
        j+=1

    print(f"Los precios son: ")
    while(k<len(precio_compra)):
        print(precio_compra[k])
        k+=1
    print(" ")
    print("Las ventas mas el 10% es: ")
    while(o<len(precio_compra)):
        precio_venta= round(precio_compra[o]*1.1,2)
        print(precio_venta)
        o+=1

if __name__ == "__main__":
    compra()