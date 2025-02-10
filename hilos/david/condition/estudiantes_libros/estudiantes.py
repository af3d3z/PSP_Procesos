import time
from random import random, randint
from threading import Thread, Condition


class Estudiante(Thread):
    libros = [False, False, False, False, False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        pos_libro_1 = randint(0, len(Estudiante.libros) - 1)
        pos_libro_2 = randint(0, len(Estudiante.libros) - 1)
        
        while pos_libro_1 == pos_libro_2:
            pos_libro_2 = randint(0, len(Estudiante.libros) -1)

        with Estudiante.cond:
            while Estudiante.libros[pos_libro_1] == True:
                print(f"[{self.name}] El libro {pos_libro_1} está ocupado, esperando a que se libere el recurso.")
                Estudiante.cond.wait()

            while Estudiante.libros[pos_libro_2] == True:
                print(f"{self.name} El libro {pos_libro_2} está ocupado, esperando a que se libere el recurso.")
                Estudiante.cond.wait()


            Estudiante.libros[pos_libro_2] = True
            Estudiante.libros[pos_libro_1] = True

        print(f"[{self.name}] está leyendo los libros {pos_libro_1} y {pos_libro_2}.")
        time.sleep(randint(3, 5))
        print(f"[{self.name}] ha terminado de leer los libros {pos_libro_1} y {pos_libro_2}.")

        with Estudiante.cond:
            Estudiante.libros[pos_libro_1] = False
            Estudiante.libros[pos_libro_2] = False
            Estudiante.cond.notify_all()