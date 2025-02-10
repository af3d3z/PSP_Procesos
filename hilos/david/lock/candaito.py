import random
from threading import *

class Bloquealista(Thread):
    lista = [False, False, False, False, False]
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, nombre)

    def run(self):
        print("Hilo: ", self.name, " ejecutandose.")

        pos = random.randint(0, len(self.lista)-1)

        #bloquea la ejecución
        Bloquealista.bloqueo.acquire()
        if not Bloquealista.lista[pos]:
            print("Hilo ", self.name, "toma la posición ", pos)
            Bloquealista.lista[pos] = True
        #libera la ejecución
        Bloquealista.bloqueo.release()