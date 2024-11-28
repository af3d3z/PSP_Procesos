from multiprocessing import Queue, Process

def leer_fichero(cola: Queue):
    with open("boletin2.2/nums.txt", "r") as archivo:
        for line in archivo.readlines():
            num = int(line)
            cola.put(num)
            
        cola.put(None)
        
def suma_numeros(cola: Queue):
    numero = cola.get()
    suma = 0
    while numero is not None:
        suma += numero
        numero = cola.get()
    
    print(f"Suma: {suma}")
    return suma

if __name__ == "__main__":
    queue = Queue()
    p1 = Process(target=leer_fichero, args=(queue,))
    p2 = Process(target=suma_numeros, args=(queue,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()