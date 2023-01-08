import math
from transformPic import transformPicture
def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d
        y2=y0+a*(y1-y0)/d
        x3=x2+h*(y1-y0)/d
        y3=y2-h*(x1-x0)/d

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d

        return (x3, y3, x4, y4)

def coordsToField(ferries, impact, after, debug):
    impactForDistance = impact
    if debug:print("Impact = ", impact)

    middleForDistance = 500,500
    if debug:print("middle = ",middleForDistance)
    impactForAngle = (impact[0]-middleForDistance[0],impact[1]-middleForDistance[1])
    distancefromThree = math.dist(middleForDistance,(ferries[0].x,ferries[0].y))
    multiplicator = 30/500
    distanceToBull = math.dist(middleForDistance,impactForDistance)*multiplicator
    if debug:print("distanceToBull = ", distanceToBull)
    if distanceToBull <= 0.6:
        field = "BULLSEYE"
    elif distanceToBull <= 1.59:
        field = "BULLS"
    elif distanceToBull <= 9.9:
        field = "INNERES SINGLE"
    elif distanceToBull <= 10.7:
        field = "TRIPLE"
    elif distanceToBull <= 16.2:
        field = "ÄUßERES SINGLE"
    elif distanceToBull <= 17:
        field = "DOUBLE"
    else:
        field = "RAUS"
    if debug:print(field)
    angle = math.degrees(math.atan2(impactForAngle[1],impactForAngle[0]))
    if debug:print(angle)
    if angle<0:
        angle+=360
    angle += 9
    sections = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
    sections = [6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5, 20, 1, 18, 4, 13, 6]
    section = sections[math.floor(angle / 18)]
    if debug:print(section)
    return(field,section, middleForDistance)
