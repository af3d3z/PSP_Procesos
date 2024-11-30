import os
from multiprocessing import Process, Pipe

def lector_pelis(p:Pipe, fichero, anio):
    with open(fichero, "r") as f:
        for line in f:
            peli, anio_lanzamiento = line.split(";")
            anio_lanzamiento = anio_lanzamiento.strip()
            print("Peli: " + peli, " Anio: " + anio_lanzamiento)
            if anio_lanzamiento == anio:
                print("Enviada: " + peli)
                p.send(peli)
        p.send(None)

def escritor_pelis(p: Pipe, anio):
    with open("peliculas_"+str(anio)+".txt", "w") as f:
        peli = p.recv()
        while peli is not None:
            print("Recibida: " + peli)
            f.write(peli +"\n")
            peli = p.recv()

if __name__ == '__main__':
    print(os.path.dirname(os.path.realpath(__file__)))
    anio = input("Ingresa el año de la pelicula: ")
    left, right = Pipe()
    p1 = Process(target=lector_pelis, args=(left, "pelis.txt", anio))
    p2 = Process(target=escritor_pelis, args=(right, anio))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Fin de operaciones.")