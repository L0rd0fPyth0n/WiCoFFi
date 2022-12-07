# usar queues
from Queue import Queue
import numpy as np


BufferSize = 6
memBuffer = Queue(maxsize = BufferSize)

MaxWaitTime = 1.5*60 #in s
heatProduced = 4 #watt/s

tankWaterTemp = 17

waterTankFullCapacity = 500 #ml
waterTankCurrCapacity = tankFullCapacity

sugarTankFullCapacity = 20 #g
sugarTankCurrCapacity = tankFullCapacity

pourVel = 2.5 #in ml/s #equal for coffe, milk and all other ingredients

def canBeMade(request):
    #view Tanks
    return (waterTankCurrCapacity - request.water < 0) and (sugarTankCurrCapacity - request.sugar < 0)
    

def takingTheIngredients(request):
    waterTankCurrCapacity = waterTankCurrCapacity - request.water
    sugarTankCurrCapacity = sugarTankCurrCapacity - request.sugar
    

while(True):
    request = memBuffer.get(block=True, timeout=None) #bloqueia a thread (isto) ate haver pedidos de cafe
    
    if not CanBeMade(request):
        sleep()
        waterTankCurrCapacity = tankFullCapacity
        sugarTankCurrCapacity = tankFullCapacity
        
    print("Preparing " + request + "\n")
    
    takingTheIngredients(request)
    TempDiff = request.howHot - tankWaterTemp
    
    TimeOfPour = request.water/pourVel  # base on time = Distance/vel  #time to fill the cup with the requested amount of water
    sleep(TimeOfPour + m.log(TempDiff,heatProduced))
    
    print("An" + request + " ready!\nYou have " + MaxWaitTime + " to get it!\n")
    sleep(MaxWaitTime)    
