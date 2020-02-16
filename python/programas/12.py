from microbit import *

for x in range (5):
	display.set_pixel(x,0,9)
	sleep (500)
	display.set_pixel (x,0,0)
	sleep (500)

display.clear()