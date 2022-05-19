
import serial
import time
from time import sleep

ser = serial.Serial('COM7', 115200) #replace with your com port

ser.write("config\r".encode())
ser.write("2\r".encode()) #number of screens
#---------------------------------
ser.write("screen\r".encode())
ser.write("6\r".encode()) #number of objects on screen
#---------------------------------
#object 1
ser.write("label\r".encode())
ser.write("0\r".encode()) #id
ser.write("20\r".encode()) #xstart
ser.write("20\r".encode()) #ystart
ser.write("201\r".encode()) #xend
ser.write("201\r".encode()) #yend
ser.write("27\r".encode()) #datalen
ser.write("04".encode()) #pixel scaling
ser.write("02".encode()) #hspacing
ser.write("01".encode()) #vspacing
ser.write("00".encode()) #usebg
ser.write("0000".encode()) #textcolor
ser.write("ffff".encode()) #bgcolor
ser.write("496E74656C6C6967656E7420446973706C6179\r".encode()) #string Intelligent Display

#object 2 - CTU lion with white bg
ser.write("picture\r".encode())
ser.write("1\r".encode()) #id
ser.write("20\r".encode()) #xstart
ser.write("60\r".encode()) #ystart
ser.write("148\r".encode()) #xend
ser.write("157\r".encode()) #yend
ser.write("4\r".encode()) #datalen
ser.write("0000".encode()) #bitmap number
ser.write("0001\r".encode()) #scaling

#object 3 - slider
ser.write("slider\r".encode())
ser.write("2\r".encode()) #id
ser.write("20\r".encode()) #xstart
ser.write("200\r".encode()) #ystart
ser.write("270\r".encode()) #xend
ser.write("255\r".encode()) #yend
ser.write("4\r".encode()) #datalen
ser.write("0007".encode()) #bitmap number
ser.write("03".encode()) #default value
ser.write("01\r".encode())#scaling

#object 4 - screenbutton
ser.write("screenbutton\r".encode())
ser.write("3\r".encode()) #id
ser.write("300\r".encode()) #xstart
ser.write("240\r".encode()) #ystart
ser.write("462\r".encode()) #xend
ser.write("286\r".encode()) #yend
ser.write("7\r".encode()) #datalen
ser.write("01".encode())   #target screen
ser.write("000A".encode()) #bitmap number for unpressed button
ser.write("000B".encode()) #bitmap number for pressed button
ser.write("0002\r".encode()) #scaling

#object 5 - button with text "°C / °F"
ser.write("button\r".encode())
ser.write("4\r".encode()) #id
ser.write("300\r".encode()) #xstart
ser.write("150\r".encode()) #ystart
ser.write("462\r".encode()) #xend
ser.write("196\r".encode()) #yend
ser.write("20\r".encode()) #datalen
ser.write("0004".encode()) #bitmap number for unpressed button
ser.write("0006".encode()) #bitmap number for pressed button
ser.write("0002".encode()) #scaling
ser.write("15".encode()) #text xoffset
ser.write("0e".encode()) #text yoffset
ser.write("03".encode()) #text scaling
ser.write("02".encode()) #text hspacing
ser.write("02".encode()) #text vspacing
ser.write("0000".encode()) #text color
ser.write("F843202F20F846\r".encode()) #°C / °F

#object 6 - interactive label for printing external data
#!!! Use background, so its possible to redraw by sending spaces
ser.write("interactivelabel\r".encode())
ser.write("5\r".encode()) #id
ser.write("170\r".encode()) #xstart
ser.write("70\r".encode()) #ystart
ser.write("300\r".encode()) #xend
ser.write("100\r".encode()) #yend
ser.write("8\r".encode()) #datalen
ser.write("06".encode()) #pixel scaling
ser.write("02".encode()) #hspacing
ser.write("01".encode()) #vspacing
ser.write("01".encode()) #usebg
ser.write("f841".encode()) #textcolor
ser.write("ffff\r".encode()) #bgcolor
#---------------------------------
# END OF SCREEN 1
#---------------------------------

ser.write("screen\r".encode())
ser.write("2\r".encode()) #number of objects on screen

#object 1
ser.write("label\r".encode())
ser.write("0\r".encode()) #id
ser.write("20\r".encode()) #xstart
ser.write("20\r".encode()) #ystart
ser.write("201\r".encode()) #xend
ser.write("201\r".encode()) #yend
ser.write("27\r".encode()) #datalen
ser.write("04".encode()) #pixel scaling
ser.write("02".encode()) #hspacing
ser.write("01".encode()) #vspacing
ser.write("00".encode()) #usebg
ser.write("0000".encode()) #textcolor
ser.write("ffff".encode()) #bgcolor
ser.write("496E74656C6C6967656E7420446973706C6179\r".encode()) #string Intelligent Display


#object 2 - screenbutton
ser.write("screenbutton\r".encode())
ser.write("7\r".encode()) #id
ser.write("300\r".encode()) #xstart
ser.write("240\r".encode()) #ystart
ser.write("462\r".encode()) #xend
ser.write("286\r".encode()) #yend
ser.write("7\r".encode()) #datalen
ser.write("01".encode())   #target screen
ser.write("000A".encode()) #bitmap number for unpressed button
ser.write("000B".encode()) #bitmap number for pressed button
ser.write("0002\r".encode()) #scaling


while(1):
    print(ser.readline())




