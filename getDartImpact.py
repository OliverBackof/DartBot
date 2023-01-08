import cv2
import numpy as np
from transformPic import transformPicture
def getDartImpact(before, after, ferries, debug):
    for x in ferries:
        if x.id == 3:
            right = [x.x,x.y]
        if x.id == 12:
            up = [x.x,x.y]
        if x.id == 9:
            left = [x.x,x.y]
        if x.id == 6:
            down = [x.x,x.y]
    before = transformPicture(before,[left,up,right,down])
    after = transformPicture(after,[left,up,right,down])
    if debug:print(before.shape,after.shape)
    gray_frame_after = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
    #gray_frame_after = cv2.GaussianBlur(gray_frame_after, (5, 5), 0)

    gray_frame_before = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    #gray_frame_before = cv2.GaussianBlur(gray_frame_before, (5, 5), 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    #normalized_image = cv2.normalize(gray_frame_before, None, alpha=100, beta=255, norm_type=cv2.NORM_MINMAX)
    #gray_frame_after = cv2.normalize(gray_frame_after, None, alpha=100, beta=255, norm_type=cv2.NORM_MINMAX)

    normalized_image = clahe.apply(gray_frame_before)
    gray_frame_after = clahe.apply(gray_frame_after)

    if debug:cv2.imshow('davor', gray_frame_before)
    if debug:cv2.imshow('danach', normalized_image)
    if debug:cv2.waitKey(0)
    initialState = normalized_image


    differ_frame = cv2.absdiff(initialState, gray_frame_after)

    thresh_frame = cv2.threshold(differ_frame, 40, 255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    kernel = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])
    thresh_frame = cv2.filter2D(thresh_frame, -1, kernel)

    if debug:cv2.imshow("Tranformed",thresh_frame)
    if debug:cv2.waitKey(0)
    cont,_ = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if debug:image_contours = cv2.drawContours(thresh_frame, cont, -1, (0, 255, 0), 3)
    if debug:cv2.imshow('Contours', image_contours)
    if debug:cv2.waitKey(0)

    rightmost_x = 0
    rightmost_y = 0
    for cur in cont:
       if cv2.contourArea(cur) > 1000:
           for point in cur:
               x, y = point[0]
               if x > rightmost_x:
                   rightmost_x = x
                   rightmost_y = y

    return [rightmost_x,rightmost_y]
