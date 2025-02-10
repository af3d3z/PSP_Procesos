from threading import Thread, Lock, Condition


class Consumer(Thread):
    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        with Panaderia.cond:
            while Panaderia.panes == 0:
                print(self.nombre, " Esperando al pan.")
                Panaderia.cond.wait()

            Panaderia.panes -= 1
            print(self.nombre, " compró un pan.")
            Panaderia.cond.notify_all()


class Reponedor(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while Panaderia.cond:
            with Panaderia.cond:
                while Panaderia.panes > 0:
                    Panaderia.cond.wait()
                print("Reponiendo panes")
                Panaderia.panes = 7
                print("Panes disponibles!")
                Panaderia.cond.notify_all()

class Panaderia(Thread):
    cond = Condition()
    panes = 7

    def __init__(self):
        Thread.__init__(self)


