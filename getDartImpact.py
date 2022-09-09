import cv2
def getDartImpact(before,after):
    print(before.shape,after.shape)
    gray_image_after = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
    gray_frame_after = cv2.GaussianBlur(gray_image_after, (21, 21), 0)

    gray_image_before = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    gray_frame_before = cv2.GaussianBlur(gray_image_before, (21, 21), 0)

    initialState = gray_frame_before


    differ_frame = cv2.absdiff(initialState, gray_frame_after)

    thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    cont,_ = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cur in cont:
       if cv2.contourArea(cur) < 200:
           continue
       bottom = tuple(cur[cur[:, :, 1].argmax()][0])
       return bottom
