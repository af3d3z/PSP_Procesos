from threading import Semaphore, Thread, Lock
from time import sleep

class Cine(Thread):
    semaforo = Semaphore(20)
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        print(f"🧍‍♂️ {self.name} 🎟️")
        Cine.semaforo.acquire()
        print(f"🧍‍♂️ {self.name} 🍿🎥")
        sleep(5)
        Cine.semaforo.release()
        print(f"🧍‍♂️ {self.name} 🎥💨")