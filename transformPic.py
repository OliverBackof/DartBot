import cv2
import numpy as np
from numpy.linalg import inv
from numpy import loadtxt
def transformPicture(image,data):
    mageMeasurement = 1000
    # Lade das Bild
    src_points = np.float32(data)
    dst_points = np.float32([[0, mageMeasurement/2], [mageMeasurement/2, 0], [mageMeasurement, mageMeasurement/2], [mageMeasurement/2, mageMeasurement]])

    # Berechne die Perspektivtransformationsmatrix
    M = cv2.getPerspectiveTransform(src_points, dst_points)
    M_inverse = inv(M)
    coord = [0, mageMeasurement/2] + [1]
    coordN = np.float32(coord)
    x = coord @ M_inverse[0]
    y = coord @ M_inverse[1]
    z = coord @ M_inverse[2]
    #print(x,y,z)
    newX = x/z
    newY = y/z
    #print(newX, newY)
    # Wandle die Perspektive des Bildes
    warped_image = cv2.warpPerspective(image, M, (mageMeasurement, mageMeasurement))
    return warped_image
