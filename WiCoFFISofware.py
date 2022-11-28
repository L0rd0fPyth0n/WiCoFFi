# usar queues
from Queue import Queue
import numpy as np



BufferSize = 6
memBuffer = Queue(maxsize = BufferSize)
waitingTime = 1

waterTankFullCapacity = 500 #ml
waterTankCurrCapacity = tankFullCapacity

sugarTankFullCapacity = 20 #g
sugarTankCurrCapacity = tankFullCapacity




#pourVel =   #in ml/s #equal for coffe, milk and all other ingredients



while(True):
    request = memBuffer.get(block=True, timeout=None)
    #bloqueia a thread (isto) ate haver pedidos de cafe
    waterTankCurrCapacity = waterTankCurrCapacity - request.water
    sugarTankCurrCapacity = sugarTankCurrCapacity - request.sugar
    #sleep()  vai depender de quê? implementa o tempo da máquina fazer o café
    
    #TimeOfPour = request.water/pourVel  #time to fill the cup with the requested amount of water
    print("An" + request.coffeType + "with " + request.sugar + " gr of sugar and " + request.water + " mls of water" )
