from datetime import datetime
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


# helper = Helper()
# print(helper.time_now())
# print(Helper.time_parse(Helper,"18:30"))