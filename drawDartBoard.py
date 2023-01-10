import cv2
from coordsToField import coordsToField
def drawDartBoard(newFrame,ferries):
    for x1 in range(1000):
        print(x1)
        for y1 in range(1000):
            if (y1 %5 in [1,2]) and (x1 %5 in [1,2]):
                (a,b,c) = coordsToField(ferries,(x1,y1),newFrame,False)
                if b in [1,4,6,15,17,19,16,11,9,5] and a != "RAUS":
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (255,255,255), thickness=-1)
                if b in [20,18,13,10,2,3,7,8,14,12] and a != "RAUS":
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (0,0,0), thickness=-1)
                if a in ["DOUBLE","TRIPLE","BULLSEYE"]:
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (255,255,0), thickness=-1)
                if a == "BULLSEYE":
                    cv2.circle(newFrame,(x1,y1), radius = 1, color = (255,0,0), thickness=-1)
    return newFrame
