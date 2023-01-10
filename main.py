import cv2
from getFerries import getFerriPoints
from getFerries import ferrimerri
from isDifference import isDifference
import time
from getDartImpact import getDartImpact
from coordsToField import coordsToField
from transformPic import transformPicture
from drawDartBoard import drawDartBoard
from getClosestFields import getClosestFields
from numpy import loadtxt
import pyttsx3
engine = pyttsx3.init()
cam = cv2.VideoCapture(3)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
time.sleep(1)
debug = True
data = loadtxt('generalCalibration.csv', delimiter=',')
ferriesData = loadtxt('ferries.csv', delimiter=',')
ferries = []
for x in ferriesData:
    ferries.append(ferrimerri(x[0],x[1],x[2]))
dartNo = 0

while True:
    if dartNo == 3:
        print("Darts rausnehmen")
        time.sleep(6)
        dartNo = 0
    print("Jetzt werfen")
    # Frame before impact
    ret, oldFrame = cam.read()
    if isDifference(cam):
        if debug:print("Darteinschlag")
        time.sleep(0.3)
        # Frame after impact
        ret, newFrame = cam.read()
        oldFrame = transformPicture(oldFrame,data)
        newFrame = transformPicture(newFrame,data)
        impact = getDartImpact(oldFrame,newFrame,ferries,debug)
        for x in ferries:
            print(x.id)
            if x.id == 3.0:
                right = [x.x,x.y]
            if x.id == 12.0:
                up = [x.x,x.y]
            if x.id == 9.0:
                left = [x.x,x.y]
            if x.id == 6.0:
                down = [x.x,x.y]
        newFrame = transformPicture(newFrame,[left,up,right,down])
        field = coordsToField(ferries, impact, newFrame,debug)
        newFrame = cv2.circle(newFrame, impact, radius=3, color=(0, 0, 255), thickness=-1)
        newFrame = drawDartBoard(newFrame,ferries)
        closestFields, newFrame, failure = getClosestFields(impact,ferries,newFrame)
        print(closestFields)
        print("Confidence = ", round(failure*100,2), "%")
        if debug:newFrame = cv2.circle(newFrame, (int(field[2][0]),int(field[2][1])), radius=3, color=(0, 255, 0), thickness=-1)
        engine.say(str(field[1])+ field[0])
        engine.runAndWait()
        if debug:cv2.imshow("new",newFrame)
        if debug:cv2.waitKey(0)
        ret, oldFrame = cam.read()
        dartNo += 1
