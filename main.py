import cv2
from getFerries import getFerriPoints
from isDifference import isDifference
from getCoords import getCoords
import time
#from getDartImpact import getDartImpacts
cam = cv2.VideoCapture(3)
ret, oldFrame = cam.read()
time.sleep(1)
while True:
    ret, newFrame = cam.read()
    if isDifference(oldFrame,newFrame):
        time.sleep(1)
        cv2.imshow("old",oldFrame)
        ret, newFrame = cam.read()
        cv2.imshow("new",newFrame)
