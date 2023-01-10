import time
import pyttsx3
from getFerries import getFerriPoints
import cv2
from numpy import asarray
from numpy import savetxt
import numpy
from transformPic import transformPicture
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def calibrateNum(num):
    talk("Halte es jetzt bei der " + str(num))
    succesfull = False
    time.sleep(2)
    talk("Los")
    while not succesfull:
        ferries = getFerriPoints(cam, False, False)
        for x in ferries:
            print(x)
            if x.id == 69:
                left = [x.x,x.y]
                talk("Das war erfolgreich")
                succesfull = True
                return left


def calibrate(cam):
    left,up,right,down = None, None, None, None
    talk("Beginne mit kalibrieren")
    left = calibrateNum(11)
    up = calibrateNum(20)
    right = calibrateNum(6)
    down = calibrateNum(3)
    # define data
    data = asarray([left,up,right,down])
    # save to csv file
    savetxt('generalCalibration.csv', data, delimiter=',')





cam = cv2.VideoCapture(3)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#calibrate(cam)

ferries = getFerriPoints(cam,False,True)

temp = []
for x in ferries:
    temp.append([x.id,x.x,x.y])
    data = asarray(temp, dtype=object)
    savetxt('ferries.csv', data, delimiter=',')
