import random
import time
light = 'LOW'
program_over = False
while not program_over:
  print(light)
  gap = random.uniform(0.1, 0.5)
  time.sleep(gap)
  if light == 'HIGH':
    light = 'LOW'
  else:
    light = 'HIGH'
  #endif
#endwhile