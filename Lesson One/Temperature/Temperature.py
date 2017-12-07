# Temperature
from microbit import *

while True:
    currentTemp = temperature()
    temperatureToString = str(currentTemp)
    formattedString = temperatureToString + "degrees Celsius"
    display.scroll(formattedString)
    delay(200)
    