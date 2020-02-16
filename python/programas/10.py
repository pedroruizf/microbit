from microbit import *
on= True

while True:
	if button_b.is_pressed():
		on = not on
		sleep (200)
	if on==True:
		display.show(Image.YES)
	else:
		display.show(Image.NO)