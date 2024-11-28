from multiprocessing import Process, Queue
from time import sleep
from random import randint

def producer(q, pid):
    for i in range(10):
        if q.full():
            print(f"[P{pid}] The queque is full")
        q.put(i)
        print(f"[P{pid}] Sent {i}")
        sleep(randint(1, 5))
    q.put(None)
    print(f"[P{pid}] Producer finished")
    
def consumer(q, pid):
    while True:
        if q.empty():
            print(f"[C{pid}] The queue is empty")
        item = q.get()
        if item is None:
            break
        print(f"[C{pid}] Got {item}")
        sleep(randint(1, 5)) 
    print(f"[C{pid}] Consumer finished.")
    
if __name__ == "__main__":
    producers = []
    consumers = []
    queue = Queue(maxsize=3)
    
    for i in range (3):
        producers.append(Process(target=producer, args=(queue,i,)))
        
    for i in range(2):
        consumers.append(Process(target=consumer, args=(queue,i,)))
    
    for i in range(3):
        producers[i].start()
    for i in range(2):
        consumers[i].start()
    
    for i in range(3):
        producers[i].join()
    
    for i in range(2):
        consumers[i].join()
    
    print("All tasks have finished!")    