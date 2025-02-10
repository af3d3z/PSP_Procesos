from threading_example import *
print("Main thread")

for i in range(0, 10):
    t = MiThread(i)
    t.start()