from multiprocessing import Process, Value, Lock

def incremento(uid, variable, lock):
    for _ in range(250):
        with lock:
            print(f"[{uid}] Incrementa el valor {variable.value}")
            variable.value+=1
        
        
if __name__ == "__main__":
    num_procesos = 4
    variable=Value("i", 0)
    lock = Lock()
    procesos = []
    
    for i in range(num_procesos):
        p=Process(target=incremento, args=(i, variable,lock))
        p.start()
        procesos.append(p)
        
    for p in procesos:
        p.join()
    
    print("Resultado: ", variable.value)