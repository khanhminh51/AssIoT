from mqtt import *
from rs485 import *
import firebase_admin
from firebase_admin import credentials, db

while True:
    temp = readTemperature()
    humi = readMoisture()
    publishdata("temp", temp)
    publishdata("humi", humi)

    time.sleep(5)