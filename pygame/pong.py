### SRC - Great code

import pygame
from pygame import key
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen

size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen

pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False
x_val = 150
y_val = 200
x_direction=5
y_direction=5
padd_length=15
padd_width=60
x_padd=0 
y_padd=20
x=1
y=1

keys = pygame.key.get_pressed()

    
ball_width = 20

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
   # -- User input and controls
 
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
         
         done = True
       #End If
    ## - the up key or down key has been pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if y_padd>0:
            y_padd = y_padd - 10
        #end if
    #end if
    if keys[pygame.K_DOWN]:
        if y_padd<420:
            y_padd = y_padd + 10
        #end if
    #end if 
   ¡
   #Next event
   # -- Game logic goes after this comment
   # -- Screen background is BLACK
    screen.fill (BLACK)
   # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
    

    x_val = x_val + x_direction
    y_val = y_val + y_direction
   
    if x_val==620 or 0:
       x_direction = x_direction* -1
       y_val = y_val + y_direction
    #end if
    if y_val==460:
       y_direction = y_direction* -1
       x_val = x_val + x_direction
    #end if
    if y_val==0:
       y_direction = y_direction* -1
       x_val = x_val + x_direction
    # end if
    if 10 < x_val < 20 and y_val in range (y_padd,y_padd+60):
        x_direction = x_direction * -1
    
    if x_val==0:
        print('you lost')
        x_padd=0
        y_padd=20
        x_val = 150
        y_val = 200
        x_direction= 5
        y_direction= 5


        
    
    pygame.draw.rect(screen, WHITE, (x_padd,y_padd,padd_length,padd_width))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
   # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
 








