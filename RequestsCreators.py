import time as t
"""tony, gera um temp aleatorio,
poe isto a dormir este tempo
(com t.sleep(), provavelmente está em ms,
vé o code example q te deixei)
e depois põe uma pessoa a pedir 
á maq 1 café, repete isto em while(true)
ou até desligarmos o programa"""

class Order:
  def __init__(self, coffeType, sugarAmount, waterAmount, howHot):
    self.coffeType = coffeType
    self.sugarAmount = sugarAmount
    self.waterAmount = waterAmount
    self.howHot = howHot
  
  def consume():

