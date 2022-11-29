import random as r
import matplotlib.pyplot as plt
import numpy as np
def getSugarAmount():
    return r.choice([1, 2, 3, 4, 5])

i = 0

arr = [0,0,0,0,0]

while(i < 100000):
    n =  getSugarAmount()
    if(n -1 == 0):
        arr[n -1] = arr[n -1] + 1
    elif (n -1 == 1):
        arr[n -1] = arr[n -1] + 1
    elif (n -1 == 2):
        arr[n -1] = arr[n -1] + 1
    elif (n -1 == 3):
        arr[n -1] = arr[n -1] + 1
    elif (n -1 == 4):
        arr[n -1] = arr[n -1] + 1
    i = i + 1

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0, 5)  
plt.ylim(0, max(arr) + 1000)
plt.plot(range(0,4),arr)

plt.show()
