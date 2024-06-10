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
    
def on_relay_control(client, userdata, message):
    command = message.payload.decode()
    if message.topic == "relay1":
        if command == "255":
            setDevice1(True)
        elif command == "0":
            setDevice1(False)
    elif message.topic == "relay2":
        if command == "255":
            setDevice2(True)
        elif command == "0":
            setDevice2(False)

client.on_message = on_relay_control
