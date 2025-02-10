from raton import Raton
from threading import Event

evento = Event()
evento.set()

for i in range(5):
    r = Raton(str(i), evento)
    r.start()
    r.join()