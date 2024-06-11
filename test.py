from Scheduler import *
from datetime import *
from IrrigationTask import *
from Helper import *
import time


def HELLO_TASK():
    print(datetime.now()," Hello 1s")

def ONESHOT_TASK():
    print(datetime.now()," OneShot")

def DUMMY_TASK():
    print(datetime.now()," Dummy 2s")

irrigation_schedule = [
  {
    "cycle": 2,
    "flow1": 1,
    "flow2": 1,
    "flow3": 1,
    "pumpIn": 1,
    "area": 2,
    "isActive": True,
    "schedulerName": "LỊCH TƯỚI 1",
    "startTime": "8:13:00",
    "stopTime": "18:40:00"
  }
]


scheduler = IoT_Scheduler()
# scheduler.SCH_Add_Task(HELLO_TASK, 0, 1000)
# scheduler.SCH_Add_Task(ONESHOT_TASK, 5000, -1)
# scheduler.SCH_Add_Task(DUMMY_TASK, 3000, 2000)
taskList = {}

for schedule in irrigation_schedule:
    task = IrrigationTask(
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
    # delay = task.startTime - Helper.time_now(Helper)

    # if delay < 0:
    #     delay = DAY_IN_MILISECOND + delay
    
    task.setTaskID(scheduler.SCH_Add_Task(task.run, 0 , 1000))
    taskList[task.taskID] = task

scheduler.SCH_Start()
# print(taskList[0].name)
# for i in taskList:
#     print(i)
#     print(taskList[i].taskID)
# time.sleep(5)
# taskList[0].isActive = False
