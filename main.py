from mqtt import *
from rs485 import *

while True:
    temp = readTemperature()
    humi = readMoisture()
    if(publishdata("temp", temp)):
        print("Publish temp success")

    if(publishdata("humi", humi)):
        print("Publish humi success")

    setDevice1(True)
    time.sleep(5)