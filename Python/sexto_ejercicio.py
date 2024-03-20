from utils import es_numero_entero
def calcular_promedio(Lunes=[], Viernes=[]):
    cant_temperatura = len(Lunes)
    vector_nuevo = []
    for i in range(cant_temperatura):
        vector_nuevo.append((Lunes[i] + Viernes[i]) / 2)
    return vector_nuevo

def tomaTemperatura():
    dia= ["Lunes","Viernes"]
    cant_temperatura =es_numero_entero(input("Digita la cantidad de veces que deseen realizar la toma de temperatura por dia\n"))
    lunes=[]
    viernes=[]
    print("Toma de temperatura del dia Lunes")
    for i in range(cant_temperatura):
        temp_lun=es_numero_entero(input(f"Digita la temperatura {i+1} \n"))
        lunes.append(temp_lun)
    print("Toma de temperatura del dia Viernes")
    for i in range(cant_temperatura):
        temp_viernes=es_numero_entero(input(f"Digita la temperatura {i+1} \n"))
        viernes.append(temp_viernes)
    nuevo_vector= calcular_promedio(lunes, viernes)
    print("promedio de las temperaturas de Lunes y Viernes:")
    for i in range(len(dia)):
        print(f"Promedio del dia {dia[i]} : {nuevo_vector[i]} °C ")




if __name__ == "__main__":
    tomaTemperatura()