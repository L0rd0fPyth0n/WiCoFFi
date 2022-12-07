from matplotlib import pyplot as plt
import random as r
import RandomEvents as re
array = [0,0,0,0,0,0,0,0,0] # # = 6

count=0
maxCount = 1000000
while(count < maxCount):
    A = re.TempWater()
    if (45 > A):
         array[0] = array[0] + 1
    elif 45 <= A < 50:
        array[1] = array[1] + 1
    elif 50 <= A < 55:
        array[2] = array[2] + 1
    elif 55 <= A < 60:
        array[3] = array[3] + 1
    elif 60 <= A < 65:
        array[4] = array[4] + 1
    elif 65 <= A < 70:
        array[5] = array[5] + 1
    elif 70 <= A < 75:
        array[6] = array[6] + 1
    elif 75 <= A < 80:
        array[7] = array[7] + 1
    else:
         array[8] = array[8] + 1
    count = count + 1

arrayRelative = [0]*len(array)
i = 0
while(i < len(array)):
    arrayRelative[i] = array[i]/maxCount
    i = i + 1

plt.title('Temperatura da água')
plt.xlabel('')
plt.bar(range(len(arrayRelative)),arrayRelative)
plt.xlim(-10, 10)
plt.ylim(0, 1)
plt.show()
