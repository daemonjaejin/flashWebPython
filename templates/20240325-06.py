import numpy as np
from numpy import arange
from sys import getsizeof

print(np.arange(10))
print(arange(10))

def f():
    print("I am f function!")

f()

a = 1
print(getsizeof(a))

b = "1"
print(getsizeof(b))

print(type(None))
print(type(True))
print(type(1))
print(type(3.14))
print(type(2 + 3j))
print(type("abc"))
# print(type(1, 2, 3))
print(type([1, 2, 3]))
print(type({"A": 10, "B": 20, "C": 30}))

print(type(f))

print(type(1))
print(a.__class__)

class C(object):
    pass

c = C()

print(type(c))

x = 1

print(id(x))