from os import truncate
import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
newcolor = (33,122,199)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen

size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen

pygame.display.set_caption("MY HOUSE")
# -- Exit game flag set to false
done = False
sun_x = 40
sun_y = 100
light= "bright"

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
   # -- User input and controls
 
   for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
         
         done = True
      #End If
   #Next event
   # -- Game logic goes after this comment
   # -- Screen background is BLACK
   screen.fill (BLACK)
   if 0<sun_x<640:
      screen.fill(WHITE)
      


   
   if sun_x>640:
      screen.fill(BLACK)
      
      
      sun_x= sun_x+2
      pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)
      sun_y=((0.0004883*sun_x**2)-(0.3125*sun_x)+100)
     

   if sun_x>1000:
      sun_x=-40
   sun_x= sun_x+2
   sun_y=((0.0004883*sun_x**2)-(0.3125*sun_x)+100)
   # -- Draw here
   pygame.draw.rect(screen, BLUE, (220,330,200,150))

   pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)
   #if sun_x>690:
   #   sun_x=-40
   #sun_x= sun_x+2
   
     

      
  

   
   
   
   pygame.draw.polygon(screen, newcolor,[(220,330),(320,200),(420,330)])
   
   
   # -- flip display to reveal new position of objects
   pygame.display.flip()
   # - The clock ticks over
   clock.tick(60)
#End While - End of game loop
pygame.quit()
