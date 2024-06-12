from constants import *
from rs485 import *
from datetime import *
class IrrigationTask():
    def __init__(self, id, name, area, cycle, startTime, endTime, mix1, mix2, mix3, pumpIn, pumpOut, isActive,client):
        self.name = name
        self.cycle =  cycle
        self.startTime = startTime
        self.endTime = endTime
        self.flag = False
        self.timer = 0 # increase time every tick --> 1 tick = 0.5s
        self.state = IDLE_STATE
        self.mix1 = mix1 # time for mixer1
        self.mix2 = mix2 # time for mixer2
        self.mix3 = mix3 # time for mixer3
        self.pumpIn = pumpIn # time for pump in
        self.pumpOut = pumpOut # time for pump out
        self.area = area # ID: 4-area1, 5-area2, 6-area3
        self.isActive = isActive
        self.taskID = id
        self.processID = -1
        self.client = client
    def setValue(self, name, area, cycle, startTime, endTime, mix1, mix2, mix3, pumpIn, pumpOut, isActive):
        self.name = name
        self.cycle =  cycle
        self.startTime = startTime
        self.endTime = endTime
        self.flag = False
        self.timer = 0 # increase time every tick --> 1 tick = 0.5s
        self.state = IDLE_STATE
        self.mix1 = mix1 # time for mixer1
        self.mix2 = mix2 # time for mixer2
        self.mix3 = mix3 # time for mixer3
        self.pumpIn = pumpIn # time for pump in
        self.pumpOut = pumpOut # time for pump out
        self.area = area # ID: 4-area1, 5-area2, 6-area3
        self.isActive = isActive
    def setTaskID(self, taskID):
        self.processID = taskID

    def getTaskID(self):
        return self.processID

    def setActiveState(self, isActive):
        if self.isActive == True and isActive == False:
            # TODO: Turn off all Relay from 1..9
            set_MIX1_STATE(False)
            set_MIX2_STATE(False)
            set_MIX3_STATE(False)
            set_AREA1_STATE(False)
            set_AREA2_STATE(False)
            set_AREA3_STATE(False)
            set_PUMP_IN_STATE(False)
            set_PUMP_OUT_STATE(False)
            self.timer = 0
            self.flag  = False
            self.state = IDLE_STATE
            # TODO: publish message if need
            self.publishdata("noti", "Tạm dừng lịch tưới thành công!")
            pass
        self.isActive = isActive

    def run(self):
        if not self.isActive:
            return
        print(self.state)
        self.timer += TICK/1000
        if self.state == IDLE_STATE:
            delay = self.startTime - self.time_now()
            print(f"TaskID: {self.taskID}, delay: {delay}")
            if delay <= TICK*5 and delay >= -1 * TICK * 5:
                self.flag = True

            if self.flag == True:
                self.state = MIX1_STATE
                self.timer = 0
                self.flag = False
                print(f"TaskID: {self.taskID}, IDLE Timeout --> Next state ${self.state}")
                # TODO: Turn on Mixer1: Relay ID=1, then send notification to mobile app through Adafruit
                set_MIX1_STATE(True)
                self.publishdata("noti", "Bắt đầu trộn mixer 1")


        elif self.state == MIX1_STATE:

            if self.timer >= self.mix1:
                self.flag = True

            if self.flag == True: #timeout
                self.state = MIX2_STATE
                self.timer = 0
                self.flag = False
                print(f"TaskID: {self.taskID}, Mixer1 Timeout --> Next state ${self.state}")
                # TODO: Turn off Mixer1: Relay ID=1, then send notification to mobile app through Adafruit
                set_MIX1_STATE(False)
                self.publishdata("noti", "Trộn mixer 1 thành công!")
                # TODO: Turn on Mixer2: Relay ID=2, then send notification to mobile app through Adafruit
                set_MIX2_STATE(True)
                self.publishdata("noti", "Bắt đầu trộn mixer 2")
        elif self.state == MIX2_STATE:

            if self.timer >= self.mix2:
                self.flag = True

            if self.flag == True: #timeout
                self.state = MIX3_STATE
                self.timer = 0
                self.flag = False
                print(f"TaskID: {self.taskID}, Mixer2 Timeout --> Next state ${self.state}")
                # TODO: Turn off Mixer2: Relay ID=2, then send notification to mobile app through Adafruit
                set_MIX2_STATE(False)
                self.publishdata("noti", "Trộn mixer 2 thành công!")
                # TODO: Turn on Mixer3: Relay ID=3, then send notification to mobile app through Adafruit
                set_MIX3_STATE(True)
                self.publishdata("noti", "Bắt đầu trộn mixer 3")
        elif self.state == MIX3_STATE:

            if self.timer >= self.mix3:
                self.flag = True

            if self.flag == True: #timeout
                self.state = PUMP_IN_STATE
                self.timer = 0
                self.flag = False
                print(f"TaskID: {self.taskID}, Mixer3 Timeout --> Next state ${self.state}")
                # TODO: Turn off Mixer3: Relay ID=3, then send notification to mobile app through Adafruit
                set_MIX3_STATE(False)
                self.publishdata("noti", "Trộn mixer 3 thành công!")               
                # TODO: Turn on PUMP_IN: Relay ID=7, then send notification to mobile app through Adafruit
                set_PUMP_IN_STATE(True)
                self.publishdata("noti", "Bắt đầu bơm nước vào bể trộn")
        elif self.state == PUMP_IN_STATE:

            if self.timer >= self.pumpIn:
                self.flag = True

            if self.flag == True:
                self.state = PUMP_OUT_STATE
                self.timer = 0
                self.flag = False
                print(f"TaskID: {self.taskID}, PUMP_IN Timeout --> Next state ${self.state}")
                # TODO: Turn off PUMP_IN: Relay ID=7, then send notification to mobile app through Adafruit
                set_PUMP_IN_STATE(False)
                self.publishdata("noti", "Bơm nước vào bể trộn thành công!")               
                print(f"TaskID: {self.taskID}, OPEN area ${self.area}")
                # TODO: Turn on Area: Relay ID=self.area, then send notification to mobile app through Adafruit
                if self.area == 1:
                    set_AREA1_STATE(True)
                elif self.area ==2:
                    set_AREA2_STATE(True)
                elif self.area == 3:
                    set_AREA3_STATE(True)
                self.publishdata("noti", f"Bắt đầu bơm vào khu vực {self.area}") 
                # TODO: Turn on PUMP_OUT: Relay ID=8, then send notification to mobile app through Adafruit
                set_PUMP_OUT_STATE(True)
        elif self.state == PUMP_OUT_STATE:
            if self.timer >= self.pumpOut:
                self.flag = True
                
            if self.flag == True:
                self.cycle -= 1
                if self.cycle > 0:
                    self.state = MIX1_STATE
                    self.flag = False
                    # TODO: Turn on Mixer1, then send notification to mobile app through Adafruit
                    set_MIX1_STATE(True)
                    self.publishdata("noti","Bắt đầu lại chu kỳ, trộn mixer 1")
                else:
                    self.state = IDLE_STATE
                    self.flag = False

                    # TODO: Done, send notification to mobile 
                print(f"TaskID: {self.taskID}, PUMP_OUT Timeout --> Next state ${self.state}")
                print(f"TaskID: {self.taskID}, CLOSE area ${self.area}")

                # TODO: Turn off Area: Relay ID=self.area, then send notification to mobile app through Adafruit
                if self.area == 1:
                    set_AREA1_STATE(False)
                elif self.area ==2:
                    set_AREA2_STATE(False)
                elif self.area == 3:
                    set_AREA3_STATE(False)
                # TODO: Turn off Pump-out, then send notification to mobile app through Adafruit
                set_PUMP_OUT_STATE(False)
                self.publishdata("noti","Kết thúc lịch tưới")
                self.timer = 0
    def time_now(self):
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_second = now.second

        # Chuyển đổi giờ, phút, giây thành miligiây
        return (current_hour * 3600 + current_minute * 60 + current_second) * 1000
    def publishdata(self, sensor_type, data):
        if sensor_type == "noti":
            self.client.publish("notification", data)