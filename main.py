import cv2
from getFerries import getFerriPoints
from isDifference import isDifference
import time
from getDartImpact import getDartImpact
from coordsToField import coordsToField
from transformPic import transformPicture
from numpy import loadtxt
import pyttsx3
engine = pyttsx3.init()
cam = cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
time.sleep(1)
debug = True
data = loadtxt('calibration.csv', delimiter=',')
gotTheFerries = False
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
        if not gotTheFerries:
            ferries = getFerriPoints(cam,debug,True)
            gotTheFerries = True
        impact = getDartImpact(oldFrame,newFrame,ferries,debug)
        for x in ferries:
            if x.id == 3:
                right = [x.x,x.y]
            if x.id == 12:
                up = [x.x,x.y]
            if x.id == 9:
                left = [x.x,x.y]
            if x.id == 6:
                down = [x.x,x.y]
        newFrame = transformPicture(newFrame,[left,up,right,down])
        field = coordsToField(ferries, impact, newFrame,debug)
        newFrame = cv2.circle(newFrame, impact, radius=3, color=(0, 0, 255), thickness=-1)
        for x1 in range(1000):
            print(x1)
            for y1 in range(1000):
                (a,b,c) = coordsToField(ferries,(x1,y1),newFrame,False)
                if b in [1,4,6,15,17,19,16,11,9,5] and a != "RAUS":
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (255,0,255), thickness=-1)
                if a in ["DOUBLE","TRIPLE","BULLSEYE"]:
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (255,255,0), thickness=-1)
                if a == "BULLSEYE":
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (255,0,0), thickness=-1)
        if debug:newFrame = cv2.circle(newFrame, (int(field[2][0]),int(field[2][1])), radius=3, color=(0, 255, 0), thickness=-1)
        engine.say(str(field[1])+ field[0])
        engine.runAndWait()
        if debug:cv2.imshow("new",newFrame)
        if debug:cv2.waitKey(0)
        ret, oldFrame = cam.read()
        dartNo += 1
