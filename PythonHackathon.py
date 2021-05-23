import pygame
import math
import random

# Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

startgame = False

#intialize variables
playerpos = [width/2, height/2]
playerSpeed = 1.5

# Load images
player = pygame.image.load(r"C:\Users\yuisa\Pictures\player (2).png")
player = pygame.transform.scale(player, (75, 25))
playerDead = False

projectile = pygame.image.load(r"C:\Users\yuisa\Pictures\spikeBall.png")
projectile = pygame.transform.scale (projectile, (30,30))

background = pygame.image.load (r"C:\Users\yuisa\Pictures\spacebackground.PNG")
background = pygame.transform.scale (background, (width, height))
background.set_alpha(128)

projectileSpeed = 0.1
projectilePos = [random.uniform (5, width-5), random.uniform (5, height-5)]
projectileVel = [projectileSpeed, projectileSpeed]

enemySpeed = 0.25
enemySpawnRate = 2
difficultlyIncreaseRate = 10

enemyPos = [[random.uniform (5, width-5), random.uniform (5, height-5)]]
enemyVel = [[enemySpeed, enemySpeed]]
enemy = pygame.image.load(r"C:\Users\yuisa\Pictures\enemy.png")
enemy = pygame.transform.scale(enemy, (50, 40))

color = (255, 255, 255)
color_light = (120, 120, 120)

# dark shade of the button
color_dark = (100, 100, 100)

width = screen.get_width()
height = screen.get_height()

# defining a fonts and texts
smallfont = pygame.font.SysFont('Corbel', 35)
bigfont = pygame.font.SysFont('Corbel', 55)

title = bigfont.render('REFLECT', True, color)
text = smallfont.render('START', True, color)

restartText = bigfont.render ('GAME OVER!', True, color)
restart= smallfont.render('RESTART?' , True , color)

buttonWidth = 200
buttonHeight = 50

# collision between x of centre of object (rect or circle) and edge
def x_edge_collision(rect_x):
  if (rect_x > width or rect_x < 0):
    return True
  else:
    return False

# collision between y of centre of object (rect or circle) and edge
def y_edge_collision(rect_y):
  if (rect_y > height or rect_y < 0):
    return True
  else:
    return False

# collision between a point and a rectangle (can be used for button events)
def point_rect_collision(point_x, point_y, rect_x, rect_y, rect_width, rect_height):
  if (rect_x - rect_width <= point_x <= rect_x + rect_width and rect_y - rect_height <= point_y <= rect_y + rect_x):
    return True
  else:
    return False

# collision between circle and rectangle, where the rectangle can be rotated (still trying to figure this out)
def circle_rect_collision(circle_x, circle_y, radius, rect_x, rect_y, rect_width, rect_height):
  maxdistance = math.sqrt(pow(rect_width /2, 2) + pow(rect_height/2, 2)) + radius
  objectdistance = math.sqrt(pow(rect_x - circle_x, 2) + pow(rect_y - circle_y, 2))
  if (objectdistance < maxdistance):
    return True
  return False

def withinx(rect1_left, rect1_right, rect2_left, rect2_right):
  if (rect1_left > rect2_left and rect1_left < rect2_right or rect1_right >= rect2_left and rect1_right < rect2_right or rect2_left > rect1_left and rect2_left < rect1_right or rect2_right > rect1_left and rect2_right < rect1_right): 
    return True
  return False

def withiny(rect1_top, rect1_bottom, rect2_top, rect2_bottom):
  if (rect1_top > rect2_top and rect1_top < rect2_bottom or rect1_bottom >= rect2_top and rect1_bottom < rect2_bottom or rect2_top > rect1_top and rect2_top < rect1_bottom or rect2_bottom > rect1_top and rect2_bottom < rect1_bottom):
    return True
  return False

# collision between two rectangles
def rect_rect_collision(rect1_top, rect1_bottom, rect1_left, rect1_right, rect2_top, rect2_bottom, rect2_left, rect2_right):
  if (withinx(rect1_left, rect1_right, rect2_left, rect2_right) and withiny(rect1_top, rect1_bottom, rect2_top, rect2_bottom)):
    return True
  else:
    return False

def collided_left(rect1_left, rect1_right, rect2_left, rect2_right):
  if (withinx(rect1_left, rect1_right, rect2_left, rect2_right)): 
    if (rect1_left <= rect2_right and rect1_left >= rect2_left):
      return True
  return False

def collided_right(rect1_left, rect1_right, rect2_left, rect2_right):
  if (withinx(rect1_left, rect1_right, rect2_left, rect2_right)): 
    if (rect1_right >= rect2_left and rect1_right <= rect2_right):
      return True
  return False

def collided_top(rect1_top, rect1_bottom, rect2_top, rect2_bottom):
  if (withiny(rect1_top, rect1_bottom, rect2_top, rect2_bottom)):
    if (rect1_top <= rect2_bottom and rect1_top >= rect2_top):
      return True
  return False

def collided_bottom(rect1_top, rect1_bottom, rect2_top, rect2_bottom):
  if (withiny(rect1_top, rect1_bottom, rect2_top, rect2_bottom)):
    if (rect1_bottom >= rect2_top and rect1_bottom <= rect2_bottom):
      return True
  return False
  


#  keep looping through
while startgame == False:
    screen.blit (background, [0,0])
    # stores the (x,y) coordinates of mouse
    mouse = pygame.mouse.get_pos()

    #pygameEvents
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if width / 2 - buttonWidth / 2 <= mouse[
                    0] <= width / 2 + buttonWidth / 2 and height / 2 - buttonHeight / 2 <= mouse[
                        1] <= height / 2 + buttonHeight / 2:
                startgame = True

    # change to lighter shade when mouse button hovers over
    if width / 2 - buttonWidth / 2 <= mouse[
            0] <= width / 2 + buttonWidth / 2 and height / 2 - buttonHeight / 2 <= mouse[
                1] <= height / 2 + buttonHeight / 2:
        pygame.draw.rect(screen, color_light, [
            width / 2 - buttonWidth / 2, height / 2 - buttonHeight / 2,
            buttonWidth, buttonHeight
        ])

    else:
        pygame.draw.rect(screen, color_dark, [
            width / 2 - buttonWidth / 2, height / 2 - buttonHeight / 2,
            buttonWidth, buttonHeight
        ])

    #creating text
    screen.blit(text, (width / 2 - 45, height / 2 - 15))
    screen.blit(title, (width / 2 - 103, height / 2 - 100))

    #  update the screen
    pygame.display.flip()

score = 0
t_lastEnemySpawnedScore = 0
t_lastEnemyDifficultyIncreaseScore = 0

while startgame:

    # clear the screen before drawing it again
    screen.fill(0)
    
    screen.blit (background, [0,0])
    if playerDead == False :
      # calculate mouse position and rotation
      position = pygame.mouse.get_pos()
      angle = math.atan2(position[1] - (playerpos[1] + 32),
                        position[0] - (playerpos[0] + 26))
      playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
      playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2,
                    playerpos[1] - playerrot.get_rect().height / 2)

      #player movement
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_w]:
          playerpos[1] -= playerSpeed
      if pressed[pygame.K_s]:
          playerpos[1] += playerSpeed
      if pressed[pygame.K_a]:
          playerpos[0] -= playerSpeed
      if pressed[pygame.K_d]:
          playerpos[0] += playerSpeed
      if pressed[pygame.K_x]: #auto kill button for testing
          playerDead = True

      #update player enemy

      #spawn enemy in a random pos on the screen
      t_score = (int) (score)

      if (t_score % enemySpawnRate == 0 and t_score > 0 and t_score > t_lastEnemySpawnedScore ): 
          
          dist = 0

          #make sure enemy is far away from player to prevent instant death
          while (dist < 250):
              randx = random.sample(range(5, width-5),1)
              randy = random.sample(range(5, height-5),1)
              dist = math.sqrt( abs (playerpos1[0] - randx[0] ) ** 2 + abs (playerpos1[1] - randy [0] ) ** 2)
                  
          enemyPos.append( [randx[0], randy[0]]) 
          
          #add small variations in speed to increase difficult and create less repetitive feeling gameplay
          offsetX = random.uniform (-0.2, 0.2)
          offsetY = random.uniform (-0.2, 0.2)

          enemyVel.append([enemySpeed + offsetX,enemySpeed + offsetY]) 

          t_lastEnemySpawnedScore = t_score

      if (t_score % difficultlyIncreaseRate == 0 and t_score > 0 and t_score > t_lastEnemyDifficultyIncreaseScore): 
          enemySpeed += 0.5
          t_lastEnemyDifficultyIncreaseScore = t_score
      counter = 0
      for e in enemyPos:

          #[0] controls enemy x, [1] controls enemy y
          e[0] += enemyVel[counter][0]
          e[1] += enemyVel[counter][1]

          # make velocity negative to reflect direction
          if (e[0] > width - enemy.get_rect().width/2 - 12 or e[0] < 0):
              enemyVel[counter][0] = enemyVel[counter][0] * -1
          if (e[1] > height - enemy.get_rect().height/2 - 12 or e[1] < 0):
              enemyVel[counter][1] = enemyVel[counter][1] * -1

          counter += 1

      #update spikeBall
          
          projectilePos[0] += projectileVel[0]
          projectilePos[1] += projectileVel[1]

        #calculate collision boundaries :O
          big_rect = [playerrot.get_rect().width, playerrot.get_rect().height]

          rect1_top = projectilePos[1] - 15
          rect1_right = projectilePos[0] + 15
          rect1_bottom = projectilePos[1] + 15
          rect1_left = projectilePos[0] - 15

          rect2_top = playerpos1[1] - big_rect[1]/2
          rect2_right = playerpos1[0] + big_rect[0]/2
          rect2_bottom = playerpos1[1] + big_rect[1]/2
          rect2_left = playerpos1[0] - big_rect[0]/2

          #reflect vel when bouncing off edge of screen
          if (projectilePos [0] > width - projectile.get_rect().width/2 or projectilePos [0] < 0):
              if (projectilePos [0] > width): projectilePos [0] = width - 10
              if (projectilePos [0] < 0): projectilePos [0] = 10
              projectileVel[0] = projectileVel[0] * -1
          if (projectilePos[1]> height - projectile.get_rect().width/2 or projectilePos[1] < 0):
              if (projectilePos [1] > height): projectilePos [1] = height - 10
              if (projectilePos [1] < 0): projectilePos [1] = 10
              projectileVel[1] = projectileVel[1] * -1

         # projectile and enemy collision
          for i in range(len(enemyPos)):
            if (rect_rect_collision(rect1_top, rect1_bottom, rect1_left, rect1_right, enemyPos[i][1] - 20, enemyPos[i][1] + 20, enemyPos[i][0] - 25, enemyPos[i][0] + 25)):
              del enemyPos[i]
              del enemyVel[i]
              projectileVel[0] = projectileVel[0] * -1
              projectileVel[1] = projectileVel[1] * -1
              break
        

          #trying out reflection:
          if circle_rect_collision(projectilePos[0], projectilePos[1], 15, playerpos[0], playerpos[1], 75, 25):
            differingX = abs (projectileVel[0] - playerpos[0])
            differingY = abs (projectileVel[1] - playerpos[1])

            if (projectileVel[0] > 0) : projectileVel [0] = differingX * -1/differingY 
            if (projectileVel[1] > 0) : projectileVel [1] = differingY * -1/differingX 
            if (projectileVel[0] < 0) : projectileVel [0] = differingX /differingY 
            if (projectileVel[1] < 0) : projectileVel [1] = differingY / differingX 

            while (projectileVel [0] > 1): projectileVel [0] /= 2
            while (projectileVel [1] > 1): projectileVel [1] /= 2
            while (projectileVel [0] < -1): projectileVel [0] /= 2
            while(projectileVel [1] < -1): projectileVel [1] /= 2

           #enemy-player collision
          for i in range(len(enemyPos)):
            if (rect_rect_collision(rect2_top, rect2_bottom, rect2_left, rect2_right, enemyPos[i][1] - 20, enemyPos[i][1] + 20, enemyPos[i][0] - 25, enemyPos[i][0] + 25)):
              playerDead = True
              break



      #draw elements
      screen.blit(playerrot, playerpos1)

      for e in enemyPos:
          screen.blit(enemy, e)

      screen.blit (projectile, projectilePos)

      #score, render on top
      score += 1 * 0.01
      scoreText = smallfont.render('SCORE: ' + str((int)(score)), True, color)

      screen.blit(scoreText, (width / 2 - 70, height / 2 - 200))
    
    else:
      screen.fill(0)

        #restart menu
        # stores the (x,y) coordinates of mouse
      mouse = pygame.mouse.get_pos()
      
          # change to lighter shade when mouse button hovers over
      if width/2 - buttonWidth/2 <= mouse[0] <= width/2+buttonWidth/2 and height/2 - buttonHeight/2 <= mouse[1] <= height/2+buttonHeight/2:
          pygame.draw.rect(screen,color_light,[width/2- buttonWidth/2,height/2 - buttonHeight/2, buttonWidth,buttonHeight])

      else:
           pygame.draw.rect(screen,color_dark,[width/2 - buttonWidth/2,height/2 - buttonHeight/2, buttonWidth,buttonHeight])

      #creating text 
      screen.blit(restart, (width/2-70,height/2-15))
      screen.blit(restartText , (width/2-150,height/2-100)) 

    #  update the screen
    pygame.display.flip()

    # loop through the events
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit() 

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2 - buttonWidth/2 <= mouse[0] <= width/2+buttonWidth/2 and height/2 - buttonHeight/2 <= mouse[1] <= height/2+buttonHeight/2:
                #intialize variables
                playerpos = [100, 100]
                playerSpeed = 1.25
                playerDead = False

                projectileSpeed = 0.1
                projectilePos = [random.uniform (5, width-5), random.uniform (5, height-5)]
                projectileVel = [projectileSpeed, projectileSpeed]

                enemySpeed = 0.25
                enemySpawnRate = 2
                difficultlyIncreaseRate = 10

                enemyPos = [[random.uniform (5, width-5), random.uniform (5, height-5)]]
                enemyVel = [[enemySpeed, enemySpeed]]

                score = 0
                t_lastEnemySpawnedScore = 0
                t_lastEnemyDifficultyIncreaseScore = 0


