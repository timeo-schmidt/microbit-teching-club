# Example One --> Timer
from microbit import *

currentDisplay = 0

def startTimer():
    
    global currentDisplay
    while currentDisplay > 0:
        display.show(str(currentDisplay))
        currentDisplay += -1;
        sleep(1000)
    if currentDisplay == 0:
        display.show(Image.HAPPY);


while True:
    display.show(str(currentDisplay))
    if button_a.is_pressed():
        currentDisplay += 1;
        display.show(str(currentDisplay))
        sleep(100)
    if button_b.is_pressed():
        startTimer();

        
        
        
        
