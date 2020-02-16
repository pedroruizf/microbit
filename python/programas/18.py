from microbit import *

while True:
    lectura = accelerometer.get_z()
    if lectura > 200:
        display.show("U")
    elif lectura < -200:
        display.show("D")
    else:
        display.show("-")
        sleep(500)