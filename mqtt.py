import sys
from Adafruit_IO import MQTTClient
import time
from rs485 import *

AIO_FEED_IDs = ["mix1", "mix2", "mix3", "area1", "area2", "area3", "pump-in", "pump-out"]
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
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
    if feed_id == "mix1":
        if payload == "255":
            print("Mixer 1 on")
            print(set_MIX1_STATE(True))
        elif payload == "0":
            print("Mixer 1 off")
            print(set_MIX1_STATE(False))
    elif feed_id == "mix2":
        if payload == "255":
            print("Mixer 2 on")
            print(set_MIX2_STATE(True))
        elif payload == "0":
            print("Mixer 2 off")
            print(set_MIX2_STATE(False))
    elif feed_id == "mix3":
        if payload == "255":
            print("Mixer 3 on")
            print(set_MIX3_STATE(True))
        elif payload == "0":
            print("Mixer 3 off")
            print(set_MIX3_STATE(False))
    elif feed_id == "area1":
        if payload == "255":
            print("Area 1 on")
            print(set_AREA1_STATE(True))
        elif payload == "0":
            print("Area 3 off")
            print(set_AREA1_STATE(False))
    elif feed_id == "area2":
        if payload == "255":
            print("Area 2 on")
            print(set_AREA2_STATE(True))
        elif payload == "0":
            print("Area 2 off")
            print(set_AREA2_STATE(False))
    elif feed_id == "area3":
        if payload == "255":
            print("Area 3 on")
            print(set_AREA3_STATE(True))
        elif payload == "0":
            print("Area 3 off")
            print(set_AREA3_STATE(False))
    elif feed_id == "pump-in":
        if payload == "255":
            print("Pump in on")
            print(set_PUMP_IN_STATE(True))
        elif payload == "0":
            print("Pump in off")
            print(set_PUMP_IN_STATE(False))
    elif feed_id == "pump-out":
        if payload == "255":
            print("Pump out on")
            print(set_PUMP_OUT_STATE(True))
        elif payload == "0":
            print("Pump out off")
            print(set_PUMP_OUT_STATE(False))
            
client.on_message = message
