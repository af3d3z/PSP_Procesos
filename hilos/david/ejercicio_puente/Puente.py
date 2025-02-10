from random import random
from threading import Thread, Semaphore, Lock
from time import sleep


class Puente(Thread):
    semaforo_norte = Semaphore(1)
    semaforo_sur = Semaphore(1)

    def __init__(self, num, direccion):
        Thread.__init__(self, name=num)
        self.direccion = direccion

    def run(self):
        if self.direccion == 0:
            print(f"El vehículo {self.name} con dirección {self.direccion} entra al puente")
            Puente.semaforo_norte.acquire()
            Puente.semaforo_sur.acquire()
            print(f"El vehículo {self.name} cruza hacia el norte.")
            sleep(random.randint(1, 4))
            print(f"El vehículo {self.name} ha salido del puente.")
            Puente.semaforo_sur.release()
            Puente.semaforo_norte.release()
        else:
            print(f"El vehículo {self.name} con dirección {self.direccion} entra al puente")
            Puente.semaforo_norte.acquire()
            Puente.semaforo_sur.acquire()
            print(f"El vehículo {self.name} cruza hacia el sur.")
            sleep(random.randint(1, 4))
            print(f"El vehículo {self.name} ha salido del puente.")
            Puente.semaforo_sur.release()
            Puente.semaforo_norte.release()