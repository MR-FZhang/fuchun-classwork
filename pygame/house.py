import pygame
import random
import os



 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255 ,255 ,255)
#game_folder =  os.path.dirname(__file__)
#img_folder = os.path.join(game_folder, "img")
#image = pygame.image.load("pygame/snow2.png","pygame/snow.png")



class Snow(pygame.sprite.Sprite):
    def __init__(self, size , speed , color):
        global rand_colors
        rand_colors = []
        for j in range(1000):
            rand_colors.append(pygame.Color("#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])))
        print(rand_colors)
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        
        #self.image = pygame.Surface([size,size])
        #self.image.fill(WHITE) 
        self.image = pygame.Surface([size,size] )
        self.image.fill(rand_colors[color])
        #self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect()
        #self.rect.center = (self.rect.x/2,self.rect.y/2)
        self.rect.x = random.randrange(0, 700)
        self.rect.y = random.randrange(0, 500)
        self.color = rand_colors[random.randrange(0,49)]
        self.speed = speed
    #end procedure
    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y > 500:
            self.rect.y = 0
            self.image.fill(rand_colors[self.color])


   



    def update(self):
        self.rect.y =self.rect.y + self.speed
        
        if self.rect.y > 500:
            self.rect.x = random.randrange(0, 700)
            self.rect.y = 0
#end class
pygame.init()

size = (700, 500)

screen = pygame.display.set_mode(size)
scr_height = screen.get_width()
pygame.display.set_caption("Snow")
 

done = False
all_sprites_group = pygame.sprite.Group() 
number_of_flakes = 50
for x in range (number_of_flakes):
    my_snow = Snow(random.randint(6,12), random.randrange(2,5) , random.randrange(0,49))
    all_sprites_group.add(my_snow) 
print(all_sprites_group)
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
    all_sprites_group.update() 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    # --- Drawing code should go here
    # -- Draw here
    all_sprites_group.draw (screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
