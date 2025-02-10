from threading import Thread
from time import sleep
from random import randint

class Worker(Thread):
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
    
    def run(self):
        print(f"Soy {self.name} y estoy trabajando.")
        sleep(randint(1, 3))
        print(f"Soy {self.name} y he terminado de trabajar.")


if __name__ == "__main__":
    nombres = ["Morilla", "Pepe", "Juan", "Pepelu"]
    trabajadors = []
    
    for i in nombres:
        t = Worker(i)
        trabajadors.append(t)
        
    for i in trabajadors:
        i.start()

    for i in trabajadors:
        i.join()
        