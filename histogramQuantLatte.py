import RandomEvents as re
import matplotlib.pyplot as plt
import math as m

ymax = 200
ymin = -200

intervalLenght = 5

n = int((ymax + abs(ymin))/intervalLenght)
array = [0]*n

count = 0
maxCount = 1000000
while(count < maxCount):
    W = re.getLatteWaterAmount()
    array[m.floor(W/intervalLenght) - int(len(array)/2)] = array[m.floor(W/intervalLenght) - int(len(array)/2)] + 1
    count = count + 1

arrayRelative = [0]*n
i = 0
while(i < len(array)):
    arrayRelative[i] = array[i]/maxCount
    i = i + 1
    
plt.title('Tempo entre pedidos')
plt.xlabel('Quantidade de cafés')
plt.bar(range(m.floor(ymin/5),m.floor(ymin/5)+len(array)),arrayRelative)
plt.xlim(-40,40)
plt.ylim(0, 1)

plt.show()
