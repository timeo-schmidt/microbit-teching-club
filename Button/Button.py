# Button
from microbit import *

while True:
    
    while button_a.is_pressed():
        display.show(Image.HAPPY)
        sleep(100)
    
    display.clear()