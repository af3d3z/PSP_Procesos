from threading import Barrier, Thread
from time import sleep
from random import randint

class Caja(Thread):
    def __init__(self, nombre, barrera: Barrier):
        Thread.__init__(self, name=nombre)
        self.barrera = barrera
        
    def run(self):
        print(f"[{self.name}] Waiting... waiting processes: {barrera.n_waiting}")
        self.barrera.wait()
        print("Hilo: ", self.name, "entra en caja.")
        sleep(randint(1,3))
        print("Hilo: ", self.name, "sale de caja")
        

if __name__ == "__main__":
    barrera = Barrier(5)
    hilos = []
    for i in range(10):
        hilo = Caja(str(i), barrera)
        sleep(randint(1, 3))
        hilo.start()
        hilos.append(hilo)
        
    for h in hilos:
        h.join()