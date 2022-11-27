# usar queues
from Queue import Queue
import numpy as np



BufferSize = 6
memBuffer = Queue(maxsize = BufferSize)
waitingTime = 1

waterTankFullCapacity = 500 #ml
waterTankCurrCapacity = tankFullCapacity

sugarTankFullCapacity = 500 #ml
sugarTankCurrCapacity = tankFullCapacity




#pourVel = 



while(True):
    request = memBuffer.get(block=True, timeout=None)
    #bloqueia a thread ate haver pedidos de cafe
    waterTankCurrCapacity = waterTankCurrCapacity - request.water
    sugarTankCurrCapacity = sugarTankCurrCapacity - request.sugar
    #sleep()  vai depender de quê? implementa o tempo da máquina fazer o café
    print("An" + request.coffeType + "with " + request.sugar + " gr of sugar and " + request.water + " mls of water" )
