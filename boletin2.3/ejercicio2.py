from multiprocessing import Pipe, Process
from random import randint

def genera_ips(t1Left):
    for _ in range(0, 10):
        n1 = randint(0, 254)
        n2 = randint(0, 254)
        n3 = randint(0, 254)
        n4 = randint(0, 254)
        
        ip = f"{n1}.{n2}.{n3}.{n4}"
        t1Left.send(ip)
    
    t1Left.send(None)
        

def clasifica_ip (t1Right, t2Left):
    ip = t1Right.recv()
    while ip is not None:
        octetos = ip.split(".")
        primero = int(octetos[0])
        if 0 <= primero <= 223:
            t2Left.send(ip)
    
        ip = t1Right.recv()
    t2Left.send(None)
    
    
def pinta_ips(t2Right):
    ip = t2Right.recv()
    while ip is not None:
        octetos = ip.split(".")
        primero = int(octetos[0])
        if primero <= 127:
            print(f"Clase A: {ip}")
        elif primero <= 191:
            print(f"Clase B: {ip}")
        else:
            print(f"Clase C: {ip}")
            
        ip = t2Right.recv()
    
    

    
if __name__ == "__main__":
    t1Left, t1Right = Pipe()
    t2Left, t2Right = Pipe()
    p1 = Process(target=genera_ips, args=(t1Left,))
    p2 = Process(target=clasifica_ip, args=(t1Right, t2Left))
    p3 = Process(target=pinta_ips, args=(t2Right,))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()