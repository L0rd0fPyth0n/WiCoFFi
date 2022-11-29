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


pourVel = 2.5 #in ml/s #equal for coffe, milk and all other ingredients

while(True):
    request = memBuffer.get(block=True, timeout=None) #bloqueia a thread (isto) ate haver pedidos de cafe
    #view Tanks, e se tem outros ingredientes
    print("Preparing" + request)
    waterTankCurrCapacity = waterTankCurrCapacity - request.water
    sugarTankCurrCapacity = sugarTankCurrCapacity - request.sugar
    
    #TimeOfPour = request.water/pourVel  # base on time = Distance/vel  #time to fill the cup with the requested amount of water
    #sleep()  vai depender de quê? implementa o tempo da máquina fazer o café
    
    print("An" + request + " ready")
    #waits for person to remove
    
