import random as r
import math as m
from random import seed, randint,random
import matplotlib.pyplot as plt
import numpy as np


##
## discrete random variables
##

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

def getSugarAmount():
    r.choice([1, 2, 3, 4, 5])  

##
## continuous random variables
##

def timeBetweenRequest():
    LAMBDA = .0021 
    return -1*((m.log(r.random()*(-1) + 1,2.1782))/LAMBDA)

def norGeneralise(avg, stdDeviation):
    # general case for the generation of random values according normal distribution
    U1 = r.random()
    U2 = r.random()
    return avg + stdDeviation*m.sqrt(-2*m.log(U1,2.7282))*m.cos(2*m.pi*U2)

def getExpressoWaterAmount():
    return norGeneralise(50, 15)

def getCappuccinoWaterAmount():
    return norGeneralise(60, 20)

def getLatteWaterAmount():
    return norGeneralise(60,25)

def getFrappeWaterAmount():
    return norGeneralise(50, 40)

def getMoccaWaterAmount():
    return norGeneralise(160, 70)
