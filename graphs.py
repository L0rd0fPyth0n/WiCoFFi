from random import seed,randint,random
import matplotlib.pyplot as plt
import numpy as np
import math as m
import random as r

media1= 50.0
desvio_padrao1=15.0

media2= 60.0
desvio_padrao2=20.0

media3= 60.0
desvio_padrao3=25.0

media4= 40.0
desvio_padrao4=50.0

media5= 160.0
desvio_padrao5=70.0

x = np.linspace(0,200,100)

f1=(1.0/(15*np.sqrt(2.0*m.pi)))*np.exp(-0.5*((x-50)/15)*2.0)
f2=(1.0/(20*np.sqrt(2.0*m.pi)))*np.exp(-0.5*((x-60)/20)*2.0)
f3=(1.0/(25*np.sqrt(2.0*m.pi)))*np.exp(-0.5*((x-60)/25)*2.0)
f4=(1.0/(40*np.sqrt(2.0*m.pi)))*np.exp(-0.5*((x-50)/40)*2.0)
f5=(1.0/(70*np.sqrt(2.0*m.pi)))*np.exp(-0.5*((x-160)/70)*2.0)

plt.plot(x,f1)
plt.plot(x,f2)
plt.plot(x,f3)
plt.plot(x,f4)
plt.plot(x,f5)
plt.xlim(-100,100)  
plt.ylim(0, 1.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(["f1 - media=50.0 , desvio_padrao=15.0","f2 - media=60.0 , desvio_padrao=20.0","f3 - media=60.0 , desvio_padrao=25.0","f4 - media=40.0 , desvio_padrao=50.0","f5 - media=160.0 , desvio_padrao=70.0"])
plt.show()

def norGeneralise(avg, stdDeviation):
    U1 = r.random()
    U2 = r.random()
    return avg + stdDeviationm.sqrt(-2*m.log(U1,2.7282))*m.cos(2*m.piU2)

def getExpressoWaterAmount():
    return norGeneralise(50, 15)

def getCappuccinoWaterAmount():
    return norGeneralise(60, 20)

def getLatteWaterAmount():
    return norGeneralise(60,25)

def getFrappeWaterAmount():
    return norGeneralise(50, 40)

def getMochaWaterAmount():
    return norGeneralise(160, 70)
