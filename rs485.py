import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    # return commPort
    return "/dev/ttyUSB0"

try:
    ser = serial.Serial(port=getPort(), baudrate=9600)
    print("Open successfully")
except:
    print("Can not open the port")


def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        # print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0

relay1_ON  = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

def setDevice1(state):
    if state == True:
        ser.write(relay1_ON)
    else:
        ser.write(relay1_OFF)
    time.sleep(1)
    return serial_read_data(ser)


relay2_ON  = [2, 6, 0, 0, 0, 255, 201, 185]
relay2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

def setDevice2(state):
    if state == True:
        ser.write(relay2_ON)
    else:
        ser.write(relay2_OFF)
    time.sleep(1)
    return serial_read_data(ser)


# Read Temperature
soil_temperature = [10, 3, 0, 6, 0, 1, 101, 112]
def readTemperature():
    serial_read_data(ser)
    ser.write(soil_temperature)
    time.sleep(1)
    return serial_read_data(ser)

# Read Humidity
soil_moisture = [10, 3, 0, 7, 0, 1, 52, 176]
def readMoisture():
    serial_read_data(ser)
    ser.write(soil_moisture)
    time.sleep(1)
    return serial_read_data(ser)

# while True:
#     print("TEST SENSOR")
#     print(readMoisture())
#     time.sleep(1)
#     print(readTemperature())
#     time.sleep(1)

# while True:
#     setDevice2(True)
#     time.sleep(2)
#     setDevice2(False)
#     time.sleep(2)