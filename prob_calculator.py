import copy
import random


# Consider using the modules imported above.
import math
class Hat:
  def __init__(self, **data):
    self.contents = []
    for (key,value) in data.items():
     # print ( f"{key} {value}")
      for x in range(0,value):
        self.contents.append(key)
    #print(self.contents)

  def draw(self,numberOfBalls):
    drawn = []
    r = numberOfBalls
    for i in range(0,r):
      if len(self.contents) < 1:
        break;
      n = math.floor(random.random()*len(self.contents))
      ##n = random.randint(0,len(self.contents)-1)
      drawn.append(self.contents[n])
      del self.contents[n]   

    return drawn
  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  print(hat.contents)
  print(expected_balls)
  print(num_balls_drawn)
  print(f"num_experiments {num_experiments}")
  print(hat.contents)
  total = 0;
  good  = 0;
  print(f"len of hat {len(hat.contents)}")
  
  for x in range(0,num_experiments):
    #print(f"x is {x} ", end="")
    tmpList = hat.contents.copy()
    drawn = hat.draw(num_balls_drawn)
    #print(drawn,end=" ")
    cntr = {}
    for n in expected_balls:
      cntr[n] = 0
    for b in drawn:
      if cntr.get(b) is not None:
        cntr[b] += 1
    allGood = True
    for k in expected_balls.keys():
      if cntr[k] < expected_balls[k]:
        allGood = False;
        break;
    total += 1
    if allGood:
      good += 1
    #print(f"{total}   {good}")
    hat.contents = tmpList.copy()
  print(f"total {total}  good {good}")
  return good/total
