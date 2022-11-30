import random as r
import matplotlib.pyplot as plt
import numpy as np
def getSugarAmount():
    return r.choice(range(5))

i = 0

arr = [0,0,0,0,0]

while(i < 100000):
    n =  getSugarAmount()
    arr[n] = arr[n] + 1
    i = i + 1

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0, 5)  
plt.ylim(0, max(arr) + 1000)
plt.plot(range(5),arr)

plt.show()
