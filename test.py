from getFerries import getFerriPoints
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
debug = True
frame = cv2.imread("./Markers/darttranform.jpg")
grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
(thresh, gray) = cv2.threshold(grayImage, 15, 255, cv2.THRESH_BINARY)
myFerriMerris = []
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
parameters =  aruco.DetectorParameters_create()
if debug:cv2.imshow("new",gray)
if debug:cv2.waitKey(0)
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
if debug:plt.figure()
if debug:plt.imshow(frame_markers)
if debug:print("Number of Ferries detected :", len(ids), "\n Ferries detected :", ids)
for i in range(len(ids)):
    if ids[i] < 13:
        c = corners[i][0]
        if debug:plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
if debug:plt.legend()
if debug:plt.show()
