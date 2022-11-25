import random as r
import matplotlib.pyplot as plt
def getSugarAmount():
    r.choice([1, 2, 3, 4, 5])

i = 0

countOf0s = 0
countOf1s = 0
countOf2s = 0
countOf3s = 0
countOf4s = 0

while(i < 10000):
    n =  getSugarAmount()
    if(n == 0):
        countOf0s = countOf0s + 1
    elif (n == 1):
        countOf1s = countOf1s + 1
    elif (n == 2):
        countOf2s = countOf2s + 1
    elif (n == 3):
        countOf3s = countOf3s + 1
    elif (n == 4):
        countOf4s = countOf4s + 1
    i = i + 1

plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(0,countOf0s/10000)
#plt.plot(0,countOf0s)
#plt.plot(0,countOf0s)
plt.show()
