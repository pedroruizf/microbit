from microbit import *

while True:
	if temperature()>32:
		display.show(Image.YES)
	else:
		display.show(Image.NO)