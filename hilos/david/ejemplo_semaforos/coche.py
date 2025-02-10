from threading import Semaphore, Thread, Lock
from time import sleep
import random

class Coche(Thread):
    semaforo = Semaphore(5)
    lock = Lock()
    
    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print(f"🚗 Vehículo {self.name} está entrando al estacionamiento.")
        Coche.semaforo.acquire()
        print(f"🚗 Vehículo {self.name} ha encontrado sitio y va a aparcar.")
        sleep(random.randint(1, 10))
        Coche.semaforo.release()
        print(f"🚗 Vehículo {self.name} ha pagado y salido del parking. Sitios libres: {Coche.semaforo._value}")        