# usar queues
from Queue import Queue
import numpy as np


BufferSize = 6
memBuffer = Queue(maxsize = BufferSize)

heatProduced = 4 #watt/s

tankWaterTemp = 17

waterTankFullCapacity = 500 #ml
waterTankCurrCapacity = tankFullCapacity

sugarTankFullCapacity = 20 #g
sugarTankCurrCapacity = tankFullCapacity

#Chocolate, espresso e leite quente
pourVel = 2.5 #in ml/s #equal for coffe, milk and all other ingredients

def seeIfCanBeMade():
    #view Tanks, e se tem outros ingredientes, se n esperar x tempo para encher
    if(waterTankCurrCapacity - request.water < 0):
        sleep()
    if(sugarTankCurrCapacity - request.sugar < 0):
        sleep()

def takingTheIngredients():
    waterTankCurrCapacity = waterTankCurrCapacity - request.water
    sugarTankCurrCapacity = sugarTankCurrCapacity - request.sugar
    

while(True):
    request = memBuffer.get(block=True, timeout=None) #bloqueia a thread (isto) ate haver pedidos de cafe
    
    seeIfCanBeMade()

    
    print("Preparing" + request)
    
    takingTheIngredients()
    TempDiff = request.howHot - tankWaterTemp
    
    TimeOfPour = request.water/pourVel  # base on time = Distance/vel  #time to fill the cup with the requested amount of water
    sleep(TimeOfPour + m.log(TempDiff,heatProduced))  vai depender de quê? implementa o tempo da máquina fazer o café
    
    print("An" + request + " ready")
    #waits for person to remove
    
