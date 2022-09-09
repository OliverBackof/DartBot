import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

class ferrimerri:
    def __init__(self,id, x,y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return "ID = " + str(self.id)+"\nCoordinaten = "+ str(self.x)+ str(self.y)


def getFerriPoints(frame):
    myFerriMerris = []
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    #plt.figure()
    #plt.imshow(frame_markers)
    for i in range(len(ids)):
        if ids[i] not in [3,6,9,12]:
            break
        c = corners[i][0]
        temp = ferrimerri(ids[i], [c[:, 0].mean()][0], [c[:, 1].mean()][0])
        myFerriMerris.append(temp)
        c = corners[i][0]
        #plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
    #plt.legend()
    #plt.show()

    return myFerriMerris
