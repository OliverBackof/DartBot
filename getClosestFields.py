import math
import cv2
from coordsToField import coordsToField
def getClosestFields(impact,ferries,newFrame):
    possibleFields = []
    middlePoint = (500,500)
    failure,notFailure = 0,0
    actualHit = coordsToField(ferries, impact, newFrame,False)
    for x in range(1000):
        for y in range(1000):
            if math.dist((x,y),impact) < 10:
                field = coordsToField(ferries, (x,y), newFrame,False)
                cv2.circle(newFrame,(x,y), radius = 1, color = (255,255,0), thickness=-1)
                if field not in possibleFields:
                    possibleFields.append(field)

                if field == actualHit:
                    notFailure += 1
                else:
                    failure += 1


    return possibleFields,newFrame,(failure/(notFailure+failure))
