from threading import Thread, Lock, Semaphore
import random
from time import sleep

class Banco(Thread):
    semaforo = Semaphore(3)
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num
        
        
    def run(self):
        print(f"Cliente {self.num} entra al cajero")
        Banco.semaforo.acquire()
        print(f"Cliente {self.num} está siendo atendido")
        sleep(random.randint(1, 4))        
        print(f"Cliente {self.num} ha sido atendido y se va.")
        Banco.semaforo.acquire()
        

if __name__ == '__main__':
    for i in range(1, 20):
        b = Banco(i)
        b.start()