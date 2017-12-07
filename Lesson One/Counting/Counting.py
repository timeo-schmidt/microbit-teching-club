# Counting
from microbit import *


for i in range(1, 11):
    display.scroll(str(i))
    sleep(100)

display.show(Image.HAPPY)