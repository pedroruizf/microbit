from microbit import *
imagenes=[Image.HEART,Image.HEART_SMALL]

while True:
	display.show (imagenes[0])
	sleep(500)
	display.show(imagenes[1])
	sleep(500)