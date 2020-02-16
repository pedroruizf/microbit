from microbit import *

pixels=[0,2,4]

while True:
	for i in range (3):
		display.set_pixel (pixels[i],0,9)
		sleep (200)
		display.set_pixel(pixels[i],0,0)
		sleep (200)