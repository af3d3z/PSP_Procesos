from threading import Thread, Event
from time import sleep

class Empresa(Thread):
    def __init__(self, nombre:str, taquilla: Event, entradas: Event):
        Thread.__init__(self, name=nombre)
        self.taquilla = taquilla
        self.entradas = entradas
        self.nentradas = 0
        
    def run(self):
        self.taquilla.set()
        self.entradas.set()
        print("Empieza la oferta")
        sleep(5)
        print("Acaba la oferta")
        self.taquilla.clear()
        self.entradas.clear()
        sleep(5)
        print(f"Se han vendido {self.nentradas} entradas")