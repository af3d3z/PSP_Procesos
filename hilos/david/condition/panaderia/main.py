import panaderia

if __name__ == '__main__':
    p = panaderia.Panaderia()
    reponedor = panaderia.Reponedor()
    reponedor.start()
    compradores = []
    for i in range(0, 20):
        compradores.append(panaderia.Consumer(i))
        compradores[i].start()