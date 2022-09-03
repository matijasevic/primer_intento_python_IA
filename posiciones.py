from random import randint

def getPosRandom(r):
  #r es  la cantidad de cuadraditos a reemplazar
  pos = []
  i = r
  while i > 0:
    x=randint(0,9)
    y=randint(0,9)
    var = [x,y]
    if not var in pos:
      pos.append(var)
      i -= 1
      
   
  
  return pos