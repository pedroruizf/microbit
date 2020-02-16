from microbit import *
import radio

radio.on()
radio.config(group=5)

while True:
	if button_a.is_pressed():
		radio.send ("A")
	
	if button_b.is_pressed():
		radio.send("B")
	
	dato=radio.receive()
	
	if dato is not None:
		display.show(dato)
		sleep(500)
	display.clear()