#initialize weights and biases between -1 and 0
#use sigmoid activation function
import random

##################################################################

def randomise_WB():
  birds = []

  #initialize weights/biases of each bird
  for i in range(10):
    bird = [[],[],[],[],0]

    #weights1
    for i in range(3):  
        weights1 = [round(random.uniform(0,1),2),round(random.uniform(0,1),2)] 
        bird[0].append(weights1)
    
    #bias1
    bias1 = [round(random.uniform(-1,0),2),round(random.uniform(-1,0),2),round(random.uniform(-1,0),2)]

    #weight2
    weights2 = [round(random.uniform(0,1),2),round(random.uniform(0,1),2),round(random.uniform(0,1),2)]

    #bias2
    bias2 = [round(random.uniform(0,1),2)]

    bird[1] = bias1
    bird[2] = weights2
    bird[3] = bias2

    birds.append(bird)
  
  return birds

##################################################################

class bird_data():
  def __init__():
    #creates dictionary variable
    pass

  def update():
    pass
    #stores each generation inside a dictionary
  
  def summarize():
    pass
  #can summarize the average fitness of each generation, high and low of each generation...

  def plot():
    pass
  #Can plot out the fitness over generations

##################################################################

class active_birds():
  def __init__(self, list_o_birds):
    self.birds_list = list_o_birds
    self.input1 = 0
    self.input2 = 0

  def new_gen(self):
    pass
    #passes old generation of birds list to bird_data class
    #take two birds with highest fitness
    #take each weight/bias and tweek it

  def bird_decision(self):
    pass
    #pass in a single bird, x_input, y_input
    #calculates output
    #if output > 
  
  def run_game(self):
    pass
  #




"""
# Each bird in bird_list looks like this
#weight layer 1
[[x,y],
[x,y],
[x,y]]

#bias layer 1
[a,b,c]

#weight layer 2
[x,y,z]

#bias layer 2
[x]



def bird_decision(input1,input2,input3, a_bird):
  inputs = [input1,input2,input3]
  weight_list = a_bird

  for weight_index in range(len(weights_list)):
    weighted_sum += weights_list[weight_index] * inputs[weight_index]

  weighted_sum_list.append(weighted_sum)


  for number in weighted_sum:
    activation_function(weighted sum)
"""