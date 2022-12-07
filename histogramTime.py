import random as r
import math as m
import matplotlib.pyplot as plt
import RandomEvents as re


array = [0,0,0,0,0,0,0,0,0] # # = 9

count=0
maxCount = 100000
while(count < maxCount):

    T = re.timeBetweenRequest()
    if 0 < T < 0.5:
        array[0]=array[0] + 1
    elif 0.5 < T < 1:
        array[1]=array[1] + 1
    elif 1 < T < 1.5:
        array[2] = array[2] + 1
    elif 1.5 < T < 2:
        array[3] = array[3] + 1
    elif 2 < T < 2.5:
        array[4]=array[4] + 1
    elif 2.5 < T < 3:
        array[5] = array[5] + 1
    elif 3 < T < 3.5:
        array[6] = array[6] + 1
    elif 3.5 < T < 4:
        array[7] = array[7] + 1
    else:
        array[8]=array[8] + 1
    count = count +1

arrayRelative = [0]*len(array)
i = 0
while(i < len(array)):
    arrayRelative[i] = array[i]/maxCount
    i = i + 1


plt.title('Tempo entre pedidos')
plt.xlabel('Quantidade de cafés')
plt.ylabel('Tempo em minutos')
#plt.hist(array,5, rwidth=0.7)
plt.bar(range(len(arrayRelative)),arrayRelative)
#plt.plot(4,array)
plt.xlim(-4, 10)
plt.ylim(0, 1)

plt.show()
