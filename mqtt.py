import sys
from Adafruit_IO import MQTTClient
import time
from rs485 import *

AIO_FEED_IDs = ["realy1", "relay2"]
AIO_USERNAME = "minhpham51"
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
# client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

def publishdata(sensor_type, data):
    if sensor_type == "temp":
        client.publish("temperature", data)
    elif sensor_type == "humi":
        client.publish("humidity", data)
    time.sleep(1)
    
def message(client , feed_id , payload):
    if feed_id == "relay1":
        if payload == "255":
            print("Relay 1 on")
            setDevice1(True)
        elif payload == "0":
            print("Relay 1 off")
            setDevice1(False)
    elif feed_id == "relay2":
        if payload == "255":
            print("Relay 2 on")
            setDevice2(True)
        elif payload == "0":
            print("Relay 2 off")
            setDevice2(False)

client.on_message = message
