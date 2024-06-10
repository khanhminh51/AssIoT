from mqtt import *
from rs485 import *

while True:
    temp = readTemperature()
    humi = readMoisture()
    publishdata("temp", temp)
    publishdata("humi", humi)

    time.sleep(5)