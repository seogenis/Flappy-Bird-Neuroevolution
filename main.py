#initialize weights and biases between -1 and 0
#use sigmoid activation function
import pygame
import random
import math

##################################################################

def randomise_WB():
  birds = []

  #initialize weights/biases of each bird
  for i in range(10):
    bird = [[],[],[],[],0]

    #weights1
    for i in range(3):  
        weights1 = [round(random.uniform(-0.03,0.03),4),round(random.uniform(-0.03,0.03),4)]
        bird[0].append(weights1)
    
    #bias1
    bias1 = [round(random.uniform(-5,0),4),round(random.uniform(-5,0),4),round(random.uniform(-5,0),4)]

    #weight2
    weights2 = [round(random.uniform(-0.02,0.02),4),round(random.uniform(-0.02,0.02),4),round(random.uniform(-0.02,0.02),4)]

    #bias2
    bias2 = [round(random.uniform(-5,0),4)]

    bird[1] = bias1
    bird[2] = weights2
    bird[3] = bias2

    birds.append(bird)
  
  return birds


##################################################################
"""
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
"""
##################################################################

class active_birds():
  def __init__(self, list_o_birds):
    self.birds_list = list_o_birds
    self.input_x = 0
    self.input_y = 0
    

  def new_gen(self):
    ancestors = [[0,0,0,0,0],[0,0,0,0,0]]
    print(self.birds_list)
    for bird in self.birds_list:
      if bird[4] > ancestors[0][4]:
        ancestors[0] = bird
      elif bird[4] >= ancestors[1][4]:
        ancestors[1] = bird
    
    self.birds_list = ancestors
    print(len(ancestors))
    print(ancestors[0])
    print(ancestors[1])

    for i in range(4):
      previous = ancestors[0]
      bird = [[],[],[],[],1]

      for a in range(len(previous[0])):
        weights1=[]
        for b in range(len(previous[0][a])):
          weights1.append(round(previous[0][a][b] + random.uniform(-0.01,0.01),4))
        bird[0].append(weights1)
      
      for a in range(len(previous[1])):
        bird[1].append(round(previous[1][a] + random.uniform(-0.2,0.2),4))
      
      for a in range(len(previous[2])):
        bird[2].append(round(previous[2][a] + random.uniform(-0.005,0.005),4))
      
      bird[3] = [round(previous[3][0] + random.uniform(-0.2,0.2),4)]

      bird[4] = 0

      self.birds_list.append(bird)  


    for i in range(4):
      previous = ancestors[1]
      bird = [[],[],[],[],0]

      for a in range(len(previous[0])):
        weights1=[]
        for b in range(len(previous[0][a])):
          weights1.append(round(previous[0][a][b] + random.uniform(-0.005,0.005),4))
        bird[0].append(weights1)
      
      for a in range(len(previous[1])):
        bird[1].append(round(previous[1][a] + random.uniform(-0.2,0.2),4))
      
      for a in range(len(previous[2])):
        bird[2].append(round(previous[2][a] + random.uniform(-0.005,0.005),4))
      
      bird[3] = [round(previous[3][0] + random.uniform(-0.2,0.2),4)]

      bird[4] = 0

      self.birds_list.append(bird)  


    #passes old generation of birds list to bird_data class
    #take two birds with highest fitness
    #take each weight/bias and tweak it



  def bird_decision(self, bird):
    #hidden layer 1
    outputs1 = []
    weights1_sum = 0

    for i in range(len(bird[0])):
      #weighted sum
      weights1_sum += bird[0][i][0]*self.input_x + bird[0][i][1]*self.input_y + bird[1][i]
      #print(f"{bird[2][i]} times {outputs1[i]}\n{bird[2][i]} times {outputs1[i]}\n{bird[2][i]} times {outputs1[i]}\nplus {bird[3][0]}")
      #activate
      #print(f"weighted1 sum: {weights1_sum}")
      weights1_sum = 1/(1+math.exp(-weights1_sum))
      #print(f"activated1: {weights1_sum}")
      #self.num+=weights1_sum
      #self.n+=1

      #add output
      outputs1.append(weights1_sum)#average around 0.4-0.6


    #hidden layer2
    outputs2 = 0
    #weighted sum
    for i in range(len(bird[2])):
      #print(f"{bird[2][1]} times {outputs1[i]}")
      outputs2 += bird[2][i]*outputs1[i]

    outputs2 = 1/(1+math.exp(-outputs2))

    #returning
    if outputs2 >= 0.5:
      return True, outputs2
    else:
      return False, outputs2
  


  def run_game(self,bird):
    #initialising moddules in pygame
    pygame.init()

    SCREEN = pygame.display.set_mode((500,750))#setting display


    #background
    BACKGROUND_IMAGE = pygame.image.load('FlappyBirdBG.jpg')


    #Bird
    SEAN_IMAGE = pygame.image.load('SEAN_IMAGE1.png')
    sean_x = 50
    sean_y = 300
    sean_y_change = 0

    def display_sean(x,y):
        SCREEN.blit(SEAN_IMAGE, (x,y))

        
    #obstacles
    OBSTACLE_WIDTH = 70
    OBSTACLE_HEIGHT = random.randint(100, 200)
    OBSTACLE_COLOR = (211, 253, 117)
    OBSTACLE_X_CHANGE = -8
    obstacle_x = 500
    space = 150

    def display_obstacle(height):
        pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
        bottom_obstacle_height = height + space
        pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, bottom_obstacle_height, OBSTACLE_WIDTH, 585 - space - height))

        
    #Collision detection
    def collision_detection (obstacle_x, obstacle_height, sean_y, bottom_obstacle_height):
        if obstacle_x >= 50 and obstacle_x <= (50 + 64): #if the sean is at same x as obstacle
            if sean_y <= obstacle_height or sean_y >= (bottom_obstacle_height - 64):
                return True
        return False


    #Score
    score = 0
    SCORE_FONT = pygame.font.Font('freesansbold.ttf',32)

    def score_display(score):
        display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
        SCREEN.blit(display,(10,10))
        

    running = True
    while running:
      print(self.birds_list)
        
      SCREEN.fill((0,0,255))
      
      #displaying background, starts drawing image from top left corner
      SCREEN.blit(BACKGROUND_IMAGE, (0,0))
      
      #game end
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
      
      sean_y += sean_y_change
      
      if sean_y <= 0:
          sean_y = 0
      if sean_y >= 530:
          sean_y = 530
      

      obstacle_x += OBSTACLE_X_CHANGE
      if obstacle_x <= 30: 
          obstacle_x = 500
          OBSTACLE_HEIGHT = random.randint(150,350)
          score += 1
      display_obstacle(OBSTACLE_HEIGHT)
      

      #collision
      collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT - 10, sean_y, OBSTACLE_HEIGHT + space + 10)
      
      
      """
      rand = random.randint(0,2)
      if rand == 0:
        sean_y_change = -3
      elif rand == 1:
        sean_y_change = 3"""                  

      #decision making
      self.input_x = obstacle_x - sean_x
      self.input_y = OBSTACLE_HEIGHT - sean_y
      decision, the_output = self.bird_decision(bird)
      print(self.input_x,self.input_y,decision,the_output)
      if decision == True:
        sean_y_change = -5
      elif decision == False:
        sean_y_change = 5

      #index current bird
      index = self.birds_list.index(bird)

      #collision
      if collision:
        self.birds_list[index][4] = pygame.time.get_ticks()/1000
        print(index)
        print(self.birds_list[index])
        running = False

      #time

      if pygame.time.get_ticks()/1000 > 99999:
        print(index)
        print(self.birds_list[index])
        self.birds_list[index][4] = pygame.time.get_ticks()/1000
        running = False
      

      #display sean
      display_sean(sean_x, sean_y)
      
      #display score
      score_display(score)
      
      #update display   
      pygame.display.update()



    print(f"You were alive for {pygame.time.get_ticks()/1000} seconds")
    pygame.quit()

    print(f"The score is {score}")
    #copy paste normal pygame in here, except....
    #instead of the keydowns, do true/false based on bird decision
    #returns fitness of bird


a_list = randomise_WB()
a = active_birds(a_list)

"""
for i in range(1000):
  a.run_game(a.birds_list[0])
  a.run_game(a.birds_list[1])
  a.run_game(a.birds_list[2])
  a.run_game(a.birds_list[3])
  a.new_gen()
"""
generations = 20
for i in range(generations):
  for bird in a.birds_list:
    a.run_game(bird)
  
  a.new_gen()

#a.print_stuff()

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