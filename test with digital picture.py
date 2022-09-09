import cv2
from getFerries import getFerriPoints
import time
from getDartImpactTest import getDartImpactTest
from coordsToField import coordsToField
import random
import matplotlib.pyplot as plt
old = cv2.imread("./Markers/dart.png")
new = cv2.imread("./Markers/dart.png")
impact = getDartImpactTest(old, new)
while True:
    impact = (random.randrange(0,320),random.randrange(0,320))
    ferries = getFerriPoints(new)
    field = coordsToField(ferries, impact, new)
    plt.figure()
    plt.imshow(new)
    plt.plot(impact[0],impact[1], "o", label = field)
    plt.legend()
    plt.show()
