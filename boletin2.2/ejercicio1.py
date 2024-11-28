from multiprocessing import Queue, Process
import os

def sumar(q, num):
    suma = 0
    print("n=", num)
    pid = os.getpid()
    for i in range(1, num+1):
        suma += i
        print(f"[{pid}] Suma de todos los valores hasta el {i}: {suma}")

if __name__ == "__main__":
    nums = [3, 23, 43, 12, 78]
    queue = Queue(maxsize=4)
    
    for num in nums:
        p = Process(target=sumar, args=(queue, num))
        p.start()
        p.join()
        
    print("Fin de operaciones")