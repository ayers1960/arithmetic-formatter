import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **data):
    for (key,value) in data.items():
      print ( f"{key} {value}")
    self.contents = []
    pass

  def draw(self,numberOfBalls):
    pass

  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  return 0
