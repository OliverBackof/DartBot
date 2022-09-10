import cv2
from getFerries import getFerriPoints
from isDifference import isDifference
import time
from getDartImpact import getDartImpact
from coordsToField import coordsToField
import pyttsx3
engine = pyttsx3.init()
cam = cv2.VideoCapture(3)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
time.sleep(1)
debug = False
while True:
    print("Jetzt werfen")
    # Frame before impact
    ret, oldFrame = cam.read()
    if isDifference(cam):
        if debug:print("Darteinschlag")
        time.sleep(1)
        # Frame after impact
        ret, newFrame = cam.read()
        impact = getDartImpact(oldFrame,newFrame,debug)
        ferries = getFerriPoints(cam,debug)
        field = coordsToField(ferries, impact, newFrame,debug)
        newFrame = cv2.circle(newFrame, impact, radius=3, color=(0, 0, 255), thickness=-1)
        if debug:newFrame = cv2.circle(newFrame, (int(field[2][0]),int(field[2][1])), radius=3, color=(0, 255, 0), thickness=-1)
        engine.say(str(field[1])+ field[0])
        engine.runAndWait()
        if debug:cv2.imshow("new",newFrame)
        if debug:cv2.waitKey(0)
