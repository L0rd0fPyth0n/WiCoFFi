import random as r
import matplotlib.pyplot as plt
import numpy as np

def pickATypeOfCoffe():
    #P(X =x) = 0.6δ(x) + 0.15δ(x - 1) +  0.2δ(x - 2) +  0.01δ(x - 3) +  0.04δ(x - 4)
    U = r.random() # entre 0 e 1 (exclusive)
    if (U < .6):
        return 0
    elif (U < .6 + .15):
        return 1
    elif (U < .6 + .15 + .2):
        return 2
    elif (U < .6 + .15 + .2 + .01):
        return 3
    else:
        return 4
i = 0

arr = [0,0,0,0,0]

while(i < 100000):
    n =  pickATypeOfCoffe()
    arr[n] = arr[n] + 1
    i = i + 1

plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-1, 5)  
plt.ylim(0, max(arr) + 1000)
plt.bar(range(5),arr)

plt.show()
