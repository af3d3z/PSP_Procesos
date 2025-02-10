from threading import Thread, Event
from time import sleep
from random import randint

from empresa import Empresa

class Comprador(Thread):
    def __init__(self, nombre:str, taquilla:Event, entradas:Event, empresa:Empresa):
        Thread.__init__(self, name=nombre)
        self.taquilla = taquilla
        self.entradas = entradas
        self.empresa = empresa
        
    def run(self):
        compra = True
        while(not self.entradas.is_set() or not self.taquilla.is_set()) and compra:
            compra = self.entradas.wait(timeout=3)
            
        if compra:
            self.entradas.clear()
            print(f"{self.name} compra su entrada")
            sleep(randint(1, 3))
            self.empresa.nentradas += 1
            print(f"{self.name} se quita de la cola. Ticket: {self.empresa.nentradas}")
            if(self.taquilla.is_set()):
                self.entradas.set()
        else:
            print(f"{self.name} se ha quedado sin entrada")
