from empresa import Empresa
from comprador import Comprador
from threading import Event

taquilla = Event()
entradas = Event()
items = []

empresa = Empresa("Empresa", taquilla, entradas)

items.append(empresa)

for i in range(10):
    c = Comprador(str(i), taquilla, entradas, empresa)
    items.append(c)
    
for item in items:
    item.start()


for item in items:
    item.join()