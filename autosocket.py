
# https://stackoverflow.com/a/19720372/11493297

import time, serial, psutil
import serial.tools.list_ports

ports = serial.tools.list_ports.comports(include_links=False)
for port in ports :
    print('\nPort : '+ port.device)

ser = serial.Serial(port.device, 9600, timeout=1)
ser.flushInput()
ser.flushOutput()

if ser.isOpen():
    ser.close()

battery = psutil.sensors_battery()
percent = battery.percent
com = str(ser.name)

# maxbat = 97
# minbat = 30

maxbat = input("Enter Max % : ")
if maxbat == '':
    maxbat = percent+1

minbat = input("Enter Min % : ")
if minbat == '':
    minbat = percent-1

Arduino_Serial = serial.Serial(com, 9600)
while True:

    battery = psutil.sensors_battery()
    percent = battery[0]

    print(percent, '[', maxbat, ',',  minbat, ']', battery[2])
    time.sleep(3)

    if percent >= int(maxbat):
        input_data = '0'.encode()
        Arduino_Serial.write(input_data)

    if percent <= int(minbat):
        input_data = '1'.encode()
        Arduino_Serial.write(input_data)
    continue
