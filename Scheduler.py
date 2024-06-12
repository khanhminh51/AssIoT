import time
import threading
from constants import *

class Task:
    def __init__(self, _pTask,_Delay, _Period):
        self.RunMe = 0
        self.TaskID = -1
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period
        self.flag = False

class IoT_Scheduler:
    SCH_tasks_G = []
    current_index_task = 0
    Abort_tasks = []
    stopFlag = False

    def __int__(self):
        self.current_index_task = 0

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / TICK, PERIOD / TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")
        return aTask.TaskID

    def SCH_Update(self):
        try: 
            for i in range(0, len(self.SCH_tasks_G)):
                if self.SCH_tasks_G[i].Delay > 0:
                    self.SCH_tasks_G[i].Delay -= 1
                elif self.SCH_tasks_G[i].Delay < 0:
                    self.Abort_tasks.append(self.SCH_tasks_G[i])
                if self.SCH_tasks_G[i].Delay == 0:
                    self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                    self.SCH_tasks_G[i].RunMe += 1
        except:
            pass

    def SCH_Dispatch_Tasks(self):
        try:
            for i in range(0, len(self.SCH_tasks_G)):
                if self.SCH_tasks_G[i].RunMe > 0:
                    self.SCH_tasks_G[i].RunMe -= 1
                    self.SCH_tasks_G[i].pTask()
        except:
            pass

    def SCH_Delete(self):
        try:
            for del_Task_id in self.Abort_tasks:
                self.SCH_tasks_G.remove(del_Task_id)
                self.Abort_tasks.clear()
        except:
            pass


    def SCH_GenerateID(self):
        return -1
    
    
    def SCH_Engine(self):
        while not self.stopFlag:
            self.SCH_Update()
            self.SCH_Dispatch_Tasks()
            self.SCH_Delete()
            time.sleep(TICK/1000)
            
    def SCH_Start(self):
        print("SCHEDULER STARTING...")
        SCH_thread = threading.Thread(target=self.SCH_Engine)
        SCH_thread.start()
        


    def SCH_Stop(self):
        self.stopFlag = True
        print("SCHEDULER TERMINATING...")



