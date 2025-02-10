from random import randint
from threading import Thread, Lock, Event, Barrier
from time import sleep


class HiddenNumber(Thread):
    hidden_number = 0
    barrier = Barrier(10)
    lock = Lock()
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        HiddenNumber.hidden_number = randint(1, 1000)

    def run(self):
        print(int(self.hidden_number))


class Guesser(Thread):
    def __init__(self, nombre, hidden_number):
        Thread.__init__(self, name=nombre)
        self.hidden_number: HiddenNumber = hidden_number

    def run(self):
            while not hidden_number.barrier.broken:
                guess = randint(1, 1000)
                print(f"[{self.name}] Guessed: {guess}")
                with HiddenNumber.lock:
                    if guess == hidden_number.hidden_number and not hidden_number.barrier.broken:
                        print(f"[{self.name}] Guessed: {guess} and guessed right!")
                        hidden_number.barrier.abort()


if __name__ == "__main__":
    hidden_number = HiddenNumber("Hidden number")

    hidden_number.start()
    hidden_number.join()

    guessers = []
    for i in range(10):
        guessers.append(Guesser(str(i), hidden_number))

    for guesser in guessers:
        guesser.start()

    for guesser in guessers:
        guesser.join()