import sys
from Adafruit_IO import MQTTClient
import time

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
# def message(client , feed_id , payload):
#     print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
#     if feed_id == "relay1":
#         if payload == "0":
#             writeData("1")
#         else:
#             writeData("2")
#     if feed_id == "nutnhan2":
#         if payload == "0":
#             writeData("3")
#         else:
#             writeData("4")

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
    