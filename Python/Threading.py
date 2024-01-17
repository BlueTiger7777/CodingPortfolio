from threading import Thread
from functools import partial

n=None
def f(x):
    while True:
        print("a")
def g(x):
    while True:
        print("b")

Thread(target=partial (f,n)).start()
g(n)
