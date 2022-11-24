import random as r
import math as m

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


def timeBetweenRequest():
    LAMBDA = .0021 
    return -1*((m.log(r.random()*(-1) + 1,2.1782))/LAMBDA)

x = 0
while x < 6:
    print(timeBetweenRequest())
    x = x + 1
