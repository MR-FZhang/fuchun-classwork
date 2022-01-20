import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
FPS = 60
RED = (255, 0, 0)
#YELLOW =  (255, 255,0) 
YELLOW = pygame.Color('#FFFF00')
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

## -- Define the class invader which is a sprite
class Player(pygame.sprite.Sprite):
  def __init__(self, color, speed):
  # Call the sprite constructor
    super().__init__()
  # Create a sprite and fill it with colour
    self.width = 10
    self.height = 10
    self.image = pygame.Surface([self.width,self.height])
    self.image.fill(color)
    self.rect = self.image.get_rect()
    # Set the position of the sprite
    self.rect.x = 300
    self.rect.y = 300
    self.speed = speed
    self.lives = 5
    

  def player_set_speed(self , speed):
    self.speed = speed

  def player_lives(self): 
    self.lives -= 1
    print(self.lives)
  
  def player_x(self):
    return  self.rect.x
  #end function


  def update(self):
    self.rect.x += self.speed
    if self.rect.x < 0:
      self.rect.x = 0
    elif self.rect.x + self.width > 700:
      self.rect.x = 700 - self.width
    if player.lives <= 0:
      event.type == pygame.QUIT
  
  def cooldown(self):
    if self.cool_down_counter >= self.COOLDOWN:
        self.cool_down_counter = 0
    elif self.cool_down_counter > 0:  
      self.cool_down_counter += 1

  def shoot(self,bullet_group):
    self.cooldown()
    if self.cool_down_counter == 0:
        bullet = Bullets(RED, 2 , self.player_x() , self.rect.y)
        self.bullet_group.add(bullet)
        bullet_group.add(bullet)
        self.cool_down_counter = 1
        self.bullet_count -= 1
        if self.bullet_count <=0:
          bullets == False
          print(self.bullet_count)
    return bullet_group



class Invader(Player):
 # Define the constructor for invader
  def __init__(self, width, height , color , speed):
  # Call the sprite constructor
    super().__init__(color , speed)
  # Create a sprite and fill it with colour
    rand_colors = []
    for j in range(50):
      rand_colors.append(pygame.Color("#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])))
    self.height = height
    self.width =  width
    self.image = pygame.Surface([self.width,self.height])
    self.speed = speed
    self.image.fill(rand_colors[color])
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(0, 600)
    self.rect.y = random.randrange(-1400, 0)
  def update(self):
    self.rect.y+= self.speed
    if self.rect.y  - self.height > 500:
      
      invader_group.remove(self)
      player.player_lives()
      
  
      
  #end procedure
#End Class
class Bullets(pygame.sprite.Sprite):
  COOLDOWN = 30
  
  def __init__(self, color , speed, x, y, invader_grp):
  # Call the sprite constructor
    super().__init__()
  # Create a sprite and fill it with colour
    self.image = pygame.Surface([10,10])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.y = y
    self.rect.x = x
    self.speed = speed
    self.invader_grp = invader_grp
    self.cool_down_counter = 0
    self.bullet_count = 10
    self.bullet_group = pygame.sprite.Group()
    
    
  #end procedure

  def bullet_set_speed(self,speed):
    self.speed = speed
   



  
  def update(self):
    self.rect.y -= self.speed
    collide_list = pygame.sprite.spritecollide(self, self.invader_grp, True)


    for invader in collide_list:
      self.invader_grp.remove(self)

class Game():
  
  def __init__(self):
    number_of_invaders = 10 
    self.bullet_group = pygame.sprite.Group()
    self.invader_group = pygame.sprite.Group() 
    self.all_sprites_group = pygame.sprite.Group()
    self.player = Player(YELLOW,0)
    self.all_sprites_group.add (self.player)
    for invader in range (number_of_invaders):
      my_invader = Invader(10, 10 , random.randint(0,49) , 1)
      self.invader_group.add (my_invader)
      self.all_sprites_group.add (my_invader)
    self.bullet = Bullets(RED, 0 , self.player.player_x(), self.player.rect.y)
    clock = pygame.time.Clock()
    self.bullet_group = self.player.shoot(self.bullet_group)
# creat a list for the bullets and the bullets added



#Next x
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


bullets = False

# -------- Main Program Loop -----------
while not done:
     # --- Main event loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
 # -- User inputs here
      elif event.type == pygame.KEYDOWN: # - a key is down
        if event.key == pygame.K_LEFT: # - if the left key pressed
          player.player_set_speed(-5)# speed set to -3
        elif event.key == pygame.K_RIGHT: # - if the right key pressed
          player.player_set_speed(5)# speed set to 3
        elif event.key == pygame.K_SPACE:
          bullets = True
          bullet.cool_down_counter = 0
        


           
      if event.type == pygame.KEYUP: # - a key released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          player.player_set_speed(0)
        elif event.key == pygame.K_SPACE:
          bullets = False

        
        
    if bullets == True:
        bullet.shoot()

# getter setter methods
     
    

    # --- Game logic should go here
    
    all_sprites_group.update()
    bullet_group.update()
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)

    for foo in player_hit_group:
      player.lives = player.lives - 1
    

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill (BLACK)
 
    # --- Drawing code should go here
    # - Screen background is BLACK
    
# -- Draw here
    all_sprites_group.draw (screen)
    bullet_group.draw (screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    FPS = 60
    clock.tick(FPS)
 
# Close the window and quit.
pygame.quit()