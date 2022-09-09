import cv2
#def isDifferent(after,before):
before = cv2.imread("./Markers/dart.png")
after = cv2.imread("./Markers/dart2.png")
diff = ImageChops.difference(before, after)
print(diff.getbbox())
