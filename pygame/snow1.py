import pygame
import random

from pygame.draw import circle 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
NAVY = (00,00,66)
moon_y = 100
moon_x = 40
class Snow:
    def __init__(self,y):
        self.x = random.randint(0,700)
        self.y = y
        self.colour = WHITE
        self.width = 10
        self.height = 10
        #end precedure

    def draw(self):
        pygame.draw.rect(screen,self.colour,[self.x,self.y ,10,10])
    #end procedure
    def update(self,vel):
        self.y+= vel
        print(self.y)
        if self.y > 500:
           self.y= 0
           self.x = random.randint(0,700)
    # end precedure
#end class

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow")
 
# Loop until the user clicks the close button.
done = False
snow2 = Snow(1)
snow1 = Snow(10)
snow3 = Snow(5)
snow4 = Snow(3)
snow5 = Snow(0)
snow6 = Snow(8)
snow7 = Snow(6)
snow8 = Snow(2)
snow9 = Snow(9)
snow10 = Snow(16)

# snow1.y = 100 
# snow1.x= random.randint(0,700)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(NAVY)
 
    # --- Drawing code should go here

    #snow1.y = snow1.y + 10
    #pygame.draw.rect(screen, snow1.colour, [snow1.x,snow1.y,10,10])
    #if snow1.y == 500 :
    # snow1.y=0
    # snow1.x= random.randint(0,700)
    
    moon_x += 2
    pygame.draw.circle(screen, WHITE, (moon_x, moon_y),40,0)
    moon_y=((0.0004883 *moon_x**2)-(0.3125*moon_x)+100)
    snow1.update(1)
    print(snow1.y)
    snow2.draw()
    snow2.update(2)
    print(snow2.y)
    snow3.draw()
    snow3.update(3)
    print(snow3.y)
    snow4.draw()
    snow4.update(4)
    print(snow4.y)
    snow5.draw()
    snow5.update(5)
    print(snow5.y)
    snow6.draw()
    snow6.update(6)
    print(snow6.y)
    snow7.draw()
    snow7.update(7)
    print(snow7.y)
    snow8.draw()
    snow8.update(8)
    print(snow8.y)
    snow9.draw()
    snow9.update(9)
    print(snow9.y)
    snow10.draw()
    snow10.update(10)
    print(snow10.y)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()