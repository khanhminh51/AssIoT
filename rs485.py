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

IDLE_STATE_ON  = [8, 6, 0, 0, 0, 255, 201, 19] #relay8
IDLE_STATE_OFF = [8, 6, 0, 0, 0, 0, 137, 83]

def set_IDLE_STATE(state):
    if state == True:
        ser.write(IDLE_STATE_ON)
    else:
        ser.write(IDLE_STATE_OFF)
    time.sleep(1)
    return serial_read_data(ser)


MIX1_STATE_ON  = [1, 6, 0, 0, 0, 255, 201, 138] #relay1
MIX1_STATE_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

def set_MIX1_STATE(state):
    if state == True:
        ser.write(MIX1_STATE_ON)
    else:
        ser.write(MIX1_STATE_OFF)
    time.sleep(1)
    return serial_read_data(ser)


MIX2_STATE_ON  = [2, 6, 0, 0, 0, 255, 201, 185] #relay2
MIX2_STATE_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

def set_MIX2_STATE(state):
    if state == True:
        ser.write(MIX2_STATE_ON)
    else:
        ser.write(MIX2_STATE_OFF)
    time.sleep(1)
    return serial_read_data(ser)


MIX3_STATE_ON  = [3, 6, 0, 0, 0, 255, 200, 104] #relay3
MIX3_STATE_OFF = [3, 6, 0, 0, 0, 0, 136, 40]

def set_MIX3_STATE(state):
    if state == True:
        ser.write(MIX3_STATE_ON)
    else:
        ser.write(MIX3_STATE_OFF)
    time.sleep(1)
    return serial_read_data(ser)


PUMP_IN_STATE_ON  = [4, 6, 0, 0, 0, 255, 201, 223] #relay4
PUMP_IN_STATE_OFF = [4, 6, 0, 0, 0, 0, 137, 159]

def set_PUMP_IN_STATE(state):
    if state == True:
        ser.write(PUMP_IN_STATE_ON)
    else:
        ser.write(PUMP_IN_STATE_OFF)
    time.sleep(1)
    return serial_read_data(ser)

PUMP_OUT_STATE_ON  = [5, 6, 0, 0, 0, 255, 200, 14] #relay5
PUMP_OUT_STATE_OFF = [5, 6, 0, 0, 0, 0, 136, 78]

def set_PUMP_OUT_STATE(state):
    if state == True:
        ser.write(PUMP_OUT_STATE_ON)
    else:
        ser.write(PUMP_OUT_STATE_OFF)
    time.sleep(1)
    return serial_read_data(ser)

SELECTOR_ON  = [6, 6, 0, 0, 0, 255, 200, 61] #relay6
SELECTOR_OFF = [6, 6, 0, 0, 0, 0, 136, 125]

def set_SELECTOR_STATE(state):
    if state == True:
        ser.write(SELECTOR_ON)
    else:
        ser.write(SELECTOR_OFF)
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