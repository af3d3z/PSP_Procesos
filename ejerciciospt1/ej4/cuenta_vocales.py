from threading import Thread


class CuentaVocales(Thread):
    def __init__(self, fichero, vocal):
        Thread.__init__(self)
        self.fichero = fichero
        self.vocal = vocal
        self.cont = 0

    def run(self):
        with open(self.fichero, "r") as f:
            for line in f:
                for character in line:
                    if character.lower() == self.vocal:
                        self.cont += 1

        print("Contador de {} : {}".format(self.vocal, self.cont))


if __name__ == '__main__':
    contadores = []

    contadorA = CuentaVocales("fixero.txt", "a")
    contadores.append(contadorA)
    contadorE = CuentaVocales("fixero.txt", "e")
    contadores.append(contadorE)
    contadorI = CuentaVocales("fixero.txt", "i")
    contadores.append(contadorI)
    contadorO = CuentaVocales("fixero.txt", "o")
    contadores.append(contadorO)
    contadorU = CuentaVocales("fixero.txt", "u")
    contadores.append(contadorU)

    for i in contadores:
        i.start()

    for i in contadores:
        i.join()
