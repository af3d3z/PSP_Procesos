from threading import Thread, Lock

class Consumer(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

class Panaderia(Thread):
    bloqueo = Lock()
    def __init__(self):
        Thread.__init__(self)
        self.panes = 7

    def comprar_pan(self, c: Consumer):
        Panaderia.bloqueo.acquire()
        if self.panes > 0:
            self.panes -= 1
            print(c.nombre, " compró un pan.")
        else:
            print(c.nombre, " en vez de un pan se compró un petisuis")
        Panaderia.bloqueo.release()


    def venta_matutina(self):
        compradores = []
        for i in range(0, 10):
            compradores.append(Consumer(i))
            self.comprar_pan(compradores[i])
