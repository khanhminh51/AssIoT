from datetime import datetime
import json
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
    def handlepayload(self, payload):
        if not payload:
            raise ValueError("Empty payload received")
        data = json.loads(payload)
        
        # type_value = data.get("type")
        id_value = data.get("id")
        state_value = data.get("state")

        return id_value, state_value


    
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