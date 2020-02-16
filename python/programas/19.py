from microbit import *
compass.calibrate()
relojes=[Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,Image.CLOCK9,Image.CLOCK10,Image.CLOCK11,Image.CLOCK12]
while True:
    rumbo=compass.heading()
    hora=int(round((rumbo/360)*12))
    display.show(relojes[hora-1])
    sleep(1000)