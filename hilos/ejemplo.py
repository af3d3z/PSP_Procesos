from threading import Thread
from time import sleep


def imprimir_mensaje(mensaje):
    for _ in range(5):
        print(mensaje)
        sleep(0.1)
        

if __name__ == "__main__":
    hilo1 = Thread(target=imprimir_mensaje, args=("Marco",))
    hilo2 = Thread(target=imprimir_mensaje, args=("Polo",))
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()
    print("Finalizado")
