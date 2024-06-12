import sys
from Adafruit_IO import MQTTClient
import time
from rs485 import *
from Helper import *
from Scheduler import *
from IrrigationTask import *

def readTempTask():
    temp = readTemperature()   
    publishdata("temp", temp)

def readHumiTask():
    humi = readMoisture()
    publishdata("humi", humi)

AIO_FEED_IDs = ["relay", "irrigation"]
AIO_USERNAME = "minhpham51"
AIO_KEY = ""

scheduler = IoT_Scheduler()
scheduler.SCH_Add_Task(readHumiTask, 0, 5000)
scheduler.SCH_Add_Task(readTempTask, 0, 5000)
taskList = {}
scheduler.SCH_Start()

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def publishdata(sensor_type, data):
    if sensor_type == "temp":
        client.publish("temperature", data)
    elif sensor_type == "humi":
        client.publish("humidity", data)
    elif sensor_type == "noti":
        client.publish("notification", data)
    print(data)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + ", feed id: " + feed_id)
    if feed_id == "relay":
        Helper.handleRelay()
    elif feed_id == "irrigation":
        schedule = Helper.stringToJson(payload)
        if schedule["action"] == "create":
            # irrigation_schedule.append(data)
            # for schedule in irrigation_schedule:
            task = IrrigationTask(
                id=schedule["id"],
                name=schedule["schedulerName"],
                area=schedule["area"],
                cycle=schedule["cycle"],
                startTime=Helper.time_parse(Helper, schedule["startTime"]),
                endTime=Helper.time_parse(Helper, schedule["stopTime"]),
                mix1=schedule["flow1"],
                mix2=schedule["flow2"],
                mix3=schedule["flow3"],
                pumpIn=schedule["pumpIn"],
                pumpOut=schedule["pumpIn"] + schedule["flow1"] + schedule["flow2"] + schedule["flow3"],
                isActive=schedule["isActive"],
                client=client
            )
            task.setTaskID(scheduler.SCH_Add_Task(task.run, 0 , 1000))
            taskList[task.taskID] = task
            publishdata("noti", "Tạo lịch tưới thành công!")
        
        elif schedule["action"] == "update":
            task = taskList[schedule["id"]]
            task.setActiveState(False)
            task.setValue(
                name=schedule["schedulerName"],
                area=schedule["area"],
                cycle=schedule["cycle"],
                startTime=Helper.time_parse(Helper, schedule["startTime"]),
                endTime=Helper.time_parse(Helper, schedule["stopTime"]),
                mix1=schedule["flow1"],
                mix2=schedule["flow2"],
                mix3=schedule["flow3"],
                pumpIn=schedule["pumpIn"],
                pumpOut=schedule["pumpIn"] + schedule["flow1"] + schedule["flow2"] + schedule["flow3"],
                isActive=schedule["isActive"]
            )
            publishdata("noti", "Cập nhật lịch tưới thành công!")

        elif schedule["action"] == "delete":
            index_to_remove = -1
            task = taskList[schedule["id"]]
            task.setActiveState(False)
            print("Remove ID: ", task.getTaskID())
            for i, element in enumerate(scheduler.SCH_tasks_G):
                if task.processID == element.TaskID:
                    index_to_remove = i
                    break
            if index_to_remove != -1:
                del scheduler.SCH_tasks_G[index_to_remove]
                print(f"TaskID: {task.taskID} remove successfully")
                publishdata("noti", "Xóa lịch tưới thành công!")

            else:
                print("Task is not existed")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
