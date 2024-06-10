from mqtt import *
from rs485 import *

temp = readTemperature()
print(temp)
humi = readMoisture()
print(humi)

if(publishdata("temp", temp)):
    print("Publish temp success")

if(publishdata("humi", humi)):
    print("Publish humi success")