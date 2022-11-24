# usar queues

from Queue import Queue

BufferSize = 6

memBuffer = Queue(maxsize = BufferSize)
waitingTime = 1


while(True):
    request = memBuffer.get(block=True, timeout=None) #bloqueia a thread ate haver pedidos de cafe
        
