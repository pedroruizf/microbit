from microbit import *
tiempo=50;
while True:
    for y in range (0,5,1):
        for x in range (0,5,1):
            display.set_pixel(x,y,9)
            sleep (tiempo)
            display.set_pixel (x,y,0)
            sleep (tiempo)
        
    for y in range (4,-1,-1):
        for x in range (4,-1,-1):
            display.set_pixel(x,y,9)
            sleep (tiempo)
            display.set_pixel (x,y,0)
            sleep (tiempo)
display.clear()