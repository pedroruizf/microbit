from microbit import *

while True:
	luz=display.read_light_level()
	nivel=round((luz*5)/255)
	#display.scroll(nivel)
	for y in range (nivel):
		for x in range(5):
			display.set_pixel (x,y,9)
	sleep(500)
	display.clear()