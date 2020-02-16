from microbit import *
import radio

radio.on()
radio.config(group=5)

while True:
	if button_b.is_pressed():
		display.show(Image.SNAKE)
		radio.off()
		break
		
	if accelerometer.is_gesture("shake"):
		radio.send ("shake")
	gesto=radio.receive()

	if gesto is not None:
		display.show(gesto)
		sleep (500)
	display.clear()