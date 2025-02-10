from threading import Thread, Lock

class Contador(Thread):
    contador = 0
    lock = Lock()
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        while Contador.contador < 1000:
            Contador.lock.acquire()
            Contador.contador += 1
            Contador.lock.release()
            print(f"[{self.name}] -> Valor actual del contador: {Contador.contador}")
            
            
if __name__ == "__main__":
    hilos = []
    
    for i in range(10):
        counter = Contador(str(i))
        hilos.append(counter)
        
    for i in hilos:
        i.start()
    
    for i in hilos:
        i.join()
        
    print("Valor final: " + str(Contador.contador))