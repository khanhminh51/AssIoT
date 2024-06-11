from constants import *
from Helper import *
class IrrigationTask():
    def __init__(self, name, area, cycle, startTime, endTime, mix1, mix2, mix3, pumpIn, pumpOut, isActive):
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
        self.taskID = -1

    def setTaskID(self, taskID):
        self.taskID = taskID

    def setActiveState(self, isActive):
        if self.isActive == True and isActive == False:
            # TODO: Turn off all Relay from 1..9

            # TODO: publish message if need

            pass
        self.isActive = isActive

    def run(self):
        if not self.isActive:
            return
        print(self.state)
        self.timer += TICK/1000
        if self.state == IDLE_STATE:
            delay = self.startTime - Helper.time_now(Helper)
            print(f"TaskID: {self.taskID}, delay: {delay}")
            if delay < TICK and delay > -1 * TICK:
                self.flag = True

            if self.flag == True:
                self.state = MIX1_STATE
                self.timer = 0
                self.flag = False
                # TODO: Turn on Mixer1: Relay ID=1, then send notification to mobile app through Adafruit

        elif self.state == MIX1_STATE:

            if self.timer >= self.mix1:
                self.flag = True

            if self.flag == True: #timeout
                self.state = MIX2_STATE
                self.timer = 0
                self.flag = False
                # TODO: Turn off Mixer1: Relay ID=1, then send notification to mobile app through Adafruit

                # TODO: Turn on Mixer2: Relay ID=2, then send notification to mobile app through Adafruit

        elif self.state == MIX2_STATE:

            if self.timer >= self.mix2:
                self.flag = True

            if self.flag == True: #timeout
                self.state = MIX3_STATE
                self.timer = 0
                self.flag = False
                # TODO: Turn off Mixer2: Relay ID=2, then send notification to mobile app through Adafruit

                # TODO: Turn on Mixer3: Relay ID=3, then send notification to mobile app through Adafruit


        elif self.state == MIX3_STATE:

            if self.timer >= self.mix3:
                self.flag = True

            if self.flag == True: #timeout
                self.state = PUMP_IN_STATE
                self.timer = 0
                self.flag = False
                # TODO: Turn off Mixer3: Relay ID=3, then send notification to mobile app through Adafruit

                # TODO: Turn on PUMP_IN: Relay ID=7, then send notification to mobile app through Adafruit

        elif self.state == PUMP_IN_STATE:

            if self.timer >= self.pumpIn:
                self.flag = True

            if self.flag == True:
                self.state = PUMP_OUT_STATE
                self.timer = 0
                self.flag = False
                # TODO: Turn off PUMP_IN: Relay ID=7, then send notification to mobile app through Adafruit

                # TODO: Turn on Area: Relay ID=self.area, then send notification to mobile app through Adafruit

                # TODO: Turn on PUMP_OUT: Relay ID=8, then send notification to mobile app through Adafruit

        elif self.state == PUMP_OUT_STATE:
            if self.timer >= self.pumpOut:
                self.flag = True
                
            if self.flag == True:
                self.cycle -= 1
                if self.cycle > 0:
                    self.state = MIX1_STATE
                    self.flag = False
                    # TODO: Turn on Mixer1, then send notification to mobile app through Adafruit

                else:
                    self.state = IDLE_STATE
                    self.flag = False

                    # TODO: Done, send notification to mobile 

                # TODO: Turn off Area: Relay ID=self.area, then send notification to mobile app through Adafruit

                # TODO: Turn off Pump-out, then send notification to mobile app through Adafruit

                self.timer = 0