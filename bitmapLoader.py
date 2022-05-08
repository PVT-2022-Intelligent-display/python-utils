import PIL
from PIL import Image
import serial
import time
from time import sleep

COMPORT = 'COM4'                        #replace with your com port
imageName = "button_stm32ide_2.bmp"           #replace with target image name
TRANSPARENT_RGB565 = 1                  #value representing transparent color inside STM32 display
TRANSPARENT_RGB565_REPLACEMENT = 0      #pixel value to which a randomly occuring TRANSPARENT_RGB565 result should be rounded
USE_TRANSPARENCY = False                #change to true if you want to mask a colour as transparent
TRANSPARENT_PIXEL = [0, 255, 0]         #colour occuring in your bitmap to be masked out as transparent

img = PIL.Image.open("bitmap-src/" + imageName)
rgb_im = img.convert('RGB')

xsize = rgb_im.size[0]
ysize = rgb_im.size[1]

pixelList = []

print("Converting to RGB565...")
for i in range(0, ysize):
    if(i%round(ysize/10)==0):
        print(f"{i}/{ysize} rows done")
    for j in range(0, xsize):
        rgbpixel = rgb_im.getpixel((j,i))
        newPixel = TRANSPARENT_RGB565
        if (not USE_TRANSPARENCY) or rgbpixel[0] != TRANSPARENT_PIXEL[0] or rgbpixel[1] != TRANSPARENT_PIXEL[1] or rgbpixel[2] != TRANSPARENT_PIXEL[2]:
            newRed = round(31*rgbpixel[0]/255)
            newGreen = round(63*rgbpixel[1]/255)
            newBlue = round(31*rgbpixel[2]/255)
            newPixel = newBlue + (newGreen << 5) + (newRed << 11)
            if newPixel == TRANSPARENT_RGB565:
                newPixel = TRANSPARENT_RGB565_REPLACEMENT
        pixelList.append(newPixel)

print(f"{ysize}/{ysize} done. First couple of pixels are:")
topRange = 128
if len(pixelList) < topRange:
    topRange = len(pixelList)
for i in range(0, topRange):
    if i%8 == 0:
        print("")
    print(f"{pixelList[i]:04x} ", end = "")
    
print("\n\nConversion done. Press enter to send.");
input()

ser = serial.Serial(COMPORT, 115200) 

ser.write("bitmap\r".encode())
ser.write(f"{xsize}\r".encode())
ser.write(f"{ysize}\r".encode())
i = 0
for pixel in pixelList:
    ser.write(f"{pixel:04x}".encode())
    i+=1
    if(i%100==0):
        print(f"{round(100*i/len(pixelList))}% sent.")
        time.sleep(0.1)
    #print(f"write {pixel:04x}")
    
ser.write("\r".encode())

print("Bitmap sent into display. Display uart output:")
while(1):
    print(ser.readline())
