import cv2
# Runs infinitely until significant movement in camera
def isDifference(video):

    initialState = None
    while True:
       check, cur_frame = video.read()
       gray_image = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
       gray_frame = cv2.GaussianBlur(gray_image, (21, 21), 0)

       if initialState is None:
           initialState = gray_frame
           continue

       differ_frame = cv2.absdiff(initialState, gray_frame)

       thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]

       thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

       cont,_ = cv2.findContours(thresh_frame.copy(),
                          cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

       for cur in cont:
           if cv2.contourArea(cur) < 200:
               continue
           return True
