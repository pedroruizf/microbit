from microbit import *
x=2
y=2
display.set_pixel(x,y,9);
while True:
  if accelerometer.get_x()>200:
    x=x+1
    display.clear()
  elif accelerometer.get_x()<-200:
    x=x-1
    display.clear()
  elif accelerometer.get_y()>200:
    y=y-1
    display.clear()
  elif accelerometer.get_y()<-200:
    y=y+1
    display.clear()
  
  if x<0:
    x=4
  if x>4:
    x=0
  if y<0:
    y=4
  if y>4:
    y=0
  display.set_pixel(x,y,9);
  sleep (50)
  
  