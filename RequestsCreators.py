import time as t
from Queue import Queue

"""tony, gera um temp aleatorio,
poe isto a dormir este tempo
(com t.sleep(), provavelmente está em ms,
vé o code example q te deixei)
e depois põe uma pessoa a pedir 
á maq 1 café, repete isto em while(true)
ou até desligarmos o programa"""

BufferSize = 6
memBuffer = Queue(maxsize = BufferSize)


class Order:
  def __init__(self, coffeType, sugar, water, howHot):
    self.coffeType = coffeType
    self.sugar = sugar
    self.water = water
    self.howHot = howHot
  
  def __str__(self):
    return self.coffeType + "with " + self.sugar + " gr of sugar and " + self.water + " mls of water"
  #to keep working in
  #def consume():
  
#def askCoffe():
  if(memBuffer.full()):
    println("Memory buffer full, ask again later")
    # decidir em grupo como fazemos
  else

#def makeNextCoffe(): 

