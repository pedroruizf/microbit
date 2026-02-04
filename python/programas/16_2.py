from microbit import *

while True:
  luz=display.read_light_level()
  if luz <64:
    for y in range (0,5,1):
      for x in range (0,5,1):
        display.set_pixel (x,y,9)
  else:
    display.clear()
  