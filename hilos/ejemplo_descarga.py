from threading import Thread
from time import sleep

def descargar_archivo(nombre, tiempo):
    print(f"Iniciando descarga de {nombre}")
    sleep(tiempo)  # Simula tiempo de descarga
    print(f"Descarga de {nombre} completada")

if __name__ == "__main__":
    hilos = [
        Thread(target=descargar_archivo, args=("Archivo 1", 3)),
        Thread(target=descargar_archivo, args=("Archivo 2", 5)),
        Thread(target=descargar_archivo, args=("Archivo 3", 2)),
    ]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print("Todas las descargas finalizadas")
