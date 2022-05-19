import serial
import time
from time import sleep
import random

ser = serial.Serial('COM4', 115200, timeout=1) #replace with your com port

#generates random temperatures. Sends them to display in celsius.
#When it gets a message from display that button for switching between celsius
#and farenheit has been pressed, switches to sending the data in farenheit.

#Make sure that, when running this script, ST-link is connected to the correct
#pin header on display!! (see display schematic - RX2, TX2 on connector J6 (8pin vertical connector)

stupidAmericanScale = 0
lastTemp = 25.0
sleepTime = 0.5

labelId = 5

FLIP_DEBOUNCE_VALUE = 2
debounceCounter = 0

while True:
    if(debounceCounter > 0):
        debounceCounter = debounceCounter - 1
    time.sleep(sleepTime)
    lastTemp = lastTemp + random.uniform(-1.5, 1.5)
    if(lastTemp > 60.0 or lastTemp < 0.1):
        lastTemp = 25.0

    scaleIdentifier = "C"
    prepTemp = lastTemp
    if stupidAmericanScale:
        prepTemp = prepTemp*1.8 + 32.0
        scaleIdentifier = "F"

    configStr1 = f"s{labelId} {prepTemp:6.2f}"
    degree = bytearray()
    degree.append(0xf8)
    configStr2 = f"{scaleIdentifier}\r"
    print(f"{configStr1}°{configStr2}")
    ser.write(configStr1.encode())
    ser.write(degree)
    ser.write(configStr2.encode())

    incoming = ser.readline()
    print(incoming.decode('ascii'))
    if debounceCounter == 0 and (incoming == b'Type:2 ID:4\n' or incoming == b'\rType:2 ID:4\n'):
        if stupidAmericanScale:
            stupidAmericanScale = 0
        else:
            stupidAmericanScale = 1
        print("flip")
        debounceCounter = FLIP_DEBOUNCE_VALUE


    
    
