import math
def coordsToField(ferries, impact, after):
    dimensions = after.shape
    impactForDistance = impact
    impactForAngle = [impact[0]-dimensions[0]/2,impact[1]-dimensions[1]/2]
    print("Impact = ", impact)
    xC = 0
    yC = 0
    for x in ferries:
        xC += x.x
        yC += x.y
    middleForDistance = (xC/len(ferries),yC/len(ferries))
    print("middle = ",middleForDistance)
    distancefromThree = math.dist(middleForDistance,(ferries[0].x,ferries[0].y))
    multiplicator = 17/distancefromThree
    distanceToBull = math.dist(middleForDistance,impactForDistance)*multiplicator
    print("distanceToBull = ", distanceToBull)
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
    print(field)
    angle = math.degrees(math.atan2(impactForAngle[1],impactForAngle[0]))
    print(angle)
    if angle<0:
        angle+=360
    angle += 9
    sections = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
    sections = [6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5, 20, 1, 18, 4, 13]
    section = sections[math.floor(angle / 18)]
    print(section)
    return(field,section)
