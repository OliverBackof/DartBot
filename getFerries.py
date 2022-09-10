import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
debug = True
class ferrimerri:
    def __init__(self,id, x,y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return "ID = " + str(self.id)+"\nCoordinaten = "+ str(self.x)+ str(self.y)

    def __eq__(self, other):
        return self.id == other


def getFerriPoints(cam):
    ids = [0]
    while len(ids) < 4:
        ret, frame = cam.read()
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, gray) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        myFerriMerris = []
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
        parameters =  aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    if debug:plt.figure()
    if debug:plt.imshow(frame_markers)
    print("Number of Ferries detected :", len(ids), "\n Ferries detected :", ids)
    for i in range(len(ids)):
        if ids[i] < 13:
            c = corners[i][0]
            temp = ferrimerri(ids[i], [c[:, 0].mean()][0], [c[:, 1].mean()][0])
            myFerriMerris.append(temp)
            c = corners[i][0]
            if debug:plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
    if debug:plt.legend()
    if debug:plt.show()

    return myFerriMerris
