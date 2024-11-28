from multiprocessing import Process, Pipe
from random import randint

numbers = []

def sorteo(pipe: Pipe):
    while True:    
        n_premiado = randint(1, 100)
        print(f"[SORTEO] El número premiado es: {n_premiado}")

        if n_premiado in numbers:
            print(f"[SORTEO] {n_premiado} Numero repetido.")
            n_premiado = randint(1, 100)
        numbers.append(n_premiado)
        
        pipe.send(n_premiado)
        p = pipe.recv()
        if p:
            break
    pipe.close()
    
def jugador(pipe: Pipe, pid):
    creditos = 10
    while creditos > 0:
        creditos -= 1
        n_jugador = randint(1, 100)
        print(f"[J{pid}] Tiene el número {n_jugador}")
        n_sorteo = pipe.recv()
        if n_jugador == n_sorteo:
            print(f"[J{pid}] Ha ganado!")
            pipe.send(1)
            break
        elif creditos == 0:
            pipe.send(2)
            print(f"[J{pid}] Se ha quedado sin casa")
        else:
            pipe.send(0)
            print(f"[J{pid}] Tiene el {n_jugador}, no ha ganado")
    pipe.close()


if __name__ == '__main__':
    pipe_sorteo, pipe_jugador = Pipe()
    
    
    p_sorteo = Process(target=sorteo, args=(pipe_sorteo,))
    p_jugador = Process(target=jugador, args=(pipe_jugador, 0,))
 
    p_sorteo.start()
    p_jugador.start()
    
    p_sorteo.join()
    p_jugador.join()   