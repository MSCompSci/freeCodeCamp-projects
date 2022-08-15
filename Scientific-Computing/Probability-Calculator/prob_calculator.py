import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**colors):
    self.contents = []
    for i in colors:
      for x in range(colors[i]):
        self.contents.append(i)
    self.backup = tuple(self.contents)
    


  def draw(self,num):
    self.contents = list(self.backup)
    drawn=[]
    if num>(len(self.contents)-1):
      return self.contents
    for x in range(num):
      index = random.randint(0,(len(self.contents)-1))
      drawn.append(self.contents.pop(index))
    return(sorted(drawn))



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  sucesses = 0
  for x in range(num_experiments):
    drawn = hat.draw(num_balls_drawn)
    #print("Drawn:",drawn)
    #print("expected:",expected_balls)
    failed = False
    for i in expected_balls:
      count = drawn.count(i)
      expected = expected_balls[i]
      if count<expected:
        failed = True
      #print(i,count)
      #print("expected",i,expected)
    if failed == False:
      sucesses +=1
  #print("sucesses:",sucesses)
  #print("experiments:",num_experiments)
  prob = sucesses/num_experiments
  return prob
