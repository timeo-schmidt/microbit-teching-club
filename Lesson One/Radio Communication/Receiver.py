# Radio Receiver Script

from microbit import *
import radio
radio.on()

message = "my-message"
clear = Image("00000:00000:00000:00000:00000")

while True:
    receivedMessage = radio.receive()
    
    if receivedMessage == message:
        display.show(Image.HAPPY)
        sleep(1000)
        display.show(clear)
        
    sleep(50)