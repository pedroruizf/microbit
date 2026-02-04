from microbit import *
display.clear()
while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.CONFUSED)
    elif accelerometer.was_gesture('left'):
        display.show(Image.ARROW_W)
    elif accelerometer.was_gesture('right'):
        display.show(Image.ARROW_E)
    else:
        sleep (500)
        display.clear()