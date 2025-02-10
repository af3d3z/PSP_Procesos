from threading import Thread, Event
from time import sleep
from random import randint

class Raton(Thread):
    def __init__(self, nombre:str, event:Event):
        Thread.__init__(self, name=nombre)
        self.evento = event
    
    def run(self):
        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        print("El ratón", self.name, "toma el control del plato")
        sleep(randint(1, 3))
        print("El ratón", self.name, "termina de comer")
        self.evento.set()