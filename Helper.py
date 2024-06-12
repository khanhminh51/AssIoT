from datetime import datetime
import json
from rs485 import *
from Scheduler import *
from datetime import *
from IrrigationTask import *
class Helper():
    def time_now(self):
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_second = now.second

        # Chuyển đổi giờ, phút, giây thành miligiây
        return (current_hour * 3600 + current_minute * 60 + current_second) * 1000
    def time_parse(self, time):
        # Chuyển đổi chuỗi thời gian thành đối tượng datetime
        start_time = datetime.strptime(time, "%H:%M:%S")

        # Chuyển đổi giờ, phút và giây thành mili giây
        milliseconds = (start_time.hour * 3600 + start_time.minute * 60 + start_time.second) * 1000
        return milliseconds
    def stringToJson(message):
        return json.loads(message)
    

    #"{"type":"area", "id":1, "state":255}"
    def handlePayloadRelay(payload):
        if not payload:
            raise ValueError("Empty payload received")
        data = json.loads(payload)
        type_value = data.get("type")
        id_value = data.get("id")
        state_value = data.get("state")
        return type_value, id_value, state_value

    # def handlePayloadIrrigation(payload):
    #     if not payload:
    #         raise ValueError("Empty payload received")
    #     data = json.loads(payload)
    #     action_value = data.get("action")
    #     id_value = data.get("id")
    #     flow1_value = data.get("flow1")
    #     flow2_value = data.get("flow2")
    #     flow3_value = data.get("flow3")
    #     pumpIn_value = data.get("pumpIn")
    #     area_value = data.get("area")
    #     isActive_value = data.get("isActive")
    #     startTime_value = data.get("startTime")
    #     stopTime_value = data.get("stopTime")

    #    return action_value, id_value, flow1_value, flow2_value, flow3_value, pumpIn_value, area_value, isActive_value, startTime_value, stopTime_value

    def handleRelay(self,payload):
        type_value, id_value, state_value = self.handlePayloadRelay(payload)
        if type_value == "mixer":
            if id_value == 1:
                if state_value == 1:
                    print("Mixer 1 on")
                    print(set_MIX1_STATE(True))
                elif state_value == 0:
                    print("Mixer 1 off")
                    print(set_MIX1_STATE(False))
            elif id_value == 2:
                if state_value == 1:
                    print("Mixer 2 on")
                    print(set_MIX2_STATE(True))
                elif state_value == 0:
                    print("Mixer 2 off")
                    print(set_MIX2_STATE(False))
            elif id_value == 3:
                if state_value == 1:
                    print("Mixer 3 on")
                    print(set_MIX3_STATE(True))
                elif state_value == 0:
                    print("Mixer 3 off")
                    print(set_MIX3_STATE(False))
        elif type_value == "area":
            if id_value == 1:
                if state_value == 1:
                    print("Area 1 on")
                    print(set_AREA1_STATE(True))
                elif state_value == 0:
                    print("Area 1 off")
                    print(set_AREA1_STATE(False))
            elif id_value == 2:
                if state_value == 1:
                    print("Area 2 on")
                    print(set_AREA2_STATE(True))
                elif state_value == 0:
                    print("Area 2 off")
                    print(set_AREA2_STATE(False))
            elif id_value == 3:
                if state_value == 1:
                    print("Area 3 on")
                    print(set_AREA3_STATE(True))
                elif state_value == 0:
                    print("Area 3 off")
                    print(set_AREA3_STATE(False))
        elif type_value == "pump":
            if id_value == 1:
                if state_value == 1:
                    print("Pump in on")
                    print(set_PUMP_IN_STATE(True))
                elif state_value == 0:
                    print("Pump in off")
                    print(set_PUMP_IN_STATE(False))
            elif id_value == 2:
                if state_value == 1:
                    print("Pump out on")
                    print(set_PUMP_OUT_STATE(True))
                elif state_value == 0:
                    print("Pump out off")
                    print(set_PUMP_OUT_STATE(False))

    def handleIrrigation(self, payload):
        pass
    





    
# json_string = '''{
#     "cycle": 2,
#     "flow1": 1,
#     "flow2": 1,
#     "flow3": 1,
#     "pumpIn": 1,
#     "area": 2,
#     "isActive": 1,
#     "schedulerName": "LỊCH TƯỚI 1",
#     "startTime": "8:13:00",
#     "stopTime": "18:40:00"
# }'''
# print(Helper.stringToJson(json_string))
# helper = Helper()
# print(helper.time_now())
# print(Helper.time_parse(Helper,"18:30"))