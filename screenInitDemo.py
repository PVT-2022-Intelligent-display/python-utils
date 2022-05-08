import serial
import time
from time import sleep

ser = serial.Serial('COM4', 115200) #replace with your com port


ser.write("config\r".encode())
ser.write("1\r".encode()) #number of screens
#---------------------------------
ser.write("screen\r".encode())
ser.write("6\r".encode()) #number of objects on screen
#---------------------------------
#object 1
ser.write("label\r".encode())
ser.write("1\r".encode()) #id
ser.write("200\r".encode()) #xstart
ser.write("200\r".encode()) #ystart
ser.write("201\r".encode()) #xend
ser.write("201\r".encode()) #yend
ser.write("12\r".encode()) #datalen
ser.write("03".encode()) #pixel scaling
ser.write("01".encode()) #hspacing
ser.write("01".encode()) #vspacing
ser.write("00".encode()) #usebg
ser.write("aabb".encode()) #textcolor
ser.write("ffff".encode()) #bgcolor
ser.write("41424344\r".encode()) #ABCD string

#object 2 - CTU lion
ser.write("picture\r".encode())
ser.write("0\r".encode()) #id
ser.write("20\r".encode()) #xstart
ser.write("150\r".encode()) #ystart
ser.write("148\r".encode()) #xend
ser.write("247\r".encode()) #yend
ser.write("4\r".encode()) #datalen
ser.write("0000".encode()) #bitmap number
ser.write("0001\r".encode()) #scaling

#object 3 - test bitmap
ser.write("picture\r".encode())
ser.write("2\r".encode()) #id
ser.write("150\r".encode()) #xstart
ser.write("150\r".encode()) #ystart
ser.write("250\r".encode()) #xend
ser.write("170\r".encode()) #yend
ser.write("4\r".encode()) #datalen
ser.write("0001".encode()) #bitmap number
ser.write("0001\r".encode()) #scaling

#object 4 - transparency test bitmap - LED symbol
ser.write("picture\r".encode())
ser.write("2\r".encode()) #id
ser.write("120\r".encode()) #xstart
ser.write("180\r".encode()) #ystart
ser.write("211\r".encode()) #xend
ser.write("254\r".encode()) #yend
ser.write("4\r".encode()) #datalen
ser.write("0003".encode()) #bitmap number
ser.write("0001\r".encode()) #scaling

#object 5 - blank pagebutton
ser.write("screenbutton\r".encode())
ser.write("2\r".encode()) #id
ser.write("300\r".encode()) #xstart
ser.write("180\r".encode()) #ystart
ser.write("462\r".encode()) #xend
ser.write("226\r".encode()) #yend
ser.write("7\r".encode()) #datalen
ser.write("00".encode())   #target screen
ser.write("0004".encode()) #bitmap number for unpressed button
ser.write("0006".encode()) #bitmap number for pressed button
ser.write("0002\r".encode()) #scaling

#object 6 - button with text "Eject!"
ser.write("button\r".encode())
ser.write("2\r".encode()) #id
ser.write("300\r".encode()) #xstart
ser.write("240\r".encode()) #ystart
ser.write("462\r".encode()) #xend
ser.write("286\r".encode()) #yend
ser.write("19\r".encode()) #datalen
ser.write("0004".encode()) #bitmap number for unpressed button
ser.write("0006".encode()) #bitmap number for pressed button
ser.write("0002".encode()) #scaling
ser.write("24".encode()) #text xoffset
ser.write("0e".encode()) #text yoffset
ser.write("03".encode()) #text scaling
ser.write("02".encode()) #text hspacing
ser.write("02".encode()) #text vspacing
ser.write("0000".encode()) #text color
ser.write("456a65637421".encode()) #Eject!





