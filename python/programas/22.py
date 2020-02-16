def grabadora():
	buffer=str(running_time())+","+ str(temperature())+","+str(display.read_light_level())+"\r\n"
	uart.write(buffer)
	sleep (250)

from microbit import *
uart.init(115200)
buffer=("tiempo"+","+"temperatura"+","+"luz"+"\r\n")
uart.write (buffer)
graba=False
display.show (Image.NO)

while True:
	if button_a.is_pressed():
		graba=not graba
		sleep(300)
	if button_b.is_pressed():
		display.show(Image.SNAKE)
		break
	if graba==True:
		display.show (Image.YES)
		grabadora()
	else:
		display.show (Image.NO)