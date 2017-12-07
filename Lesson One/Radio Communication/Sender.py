# Radio Sender Script

from microbit import *
import radio
radio.on()

message = "my-message"
clear = Image("00000:00000:00000:00000:00000")
full = Image("99999:99999:99999:99999:99999")

while True:
    if button_a.is_pressed():
        radio.send(message)
        display.show(full)
        sleep(1000)
        display.show(clear)

    sleep(100)
