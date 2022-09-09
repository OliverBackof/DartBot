import cv2
from getFerries import getFerriPoints
from test import isDifference
import time
from getDartImpact import getDartImpact
from coordsToField import coordsToField
cam = cv2.VideoCapture(3)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
time.sleep(1)
# Checking if all Feries are Visible
ret, ferriCheck = cam.read()
ferriCheck = getFerriPoints(ferriCheck)
while True:
    print("los")
    # Frame before impact
    ret, oldFrame = cam.read()
    if isDifference(cam):
        print("Darteinschlag")
        time.sleep(1)
        # Frame after impact
        ret, newFrame = cam.read()
        impact = getDartImpact(oldFrame,newFrame)
        ferries = getFerriPoints(newFrame)
        field = coordsToField(ferries, impact, newFrame)
        cv2.imshow("old",oldFrame)
        newFrame = cv2.circle(newFrame, impact, radius=3, color=(0, 0, 255), thickness=-1)
        print(field[2])
        newFrame = cv2.circle(newFrame, (int(field[2][0]),int(field[2][1])), radius=3, color=(0, 255, 0), thickness=-1)
        cv2.imshow("new",newFrame)
        cv2.waitKey(0)
