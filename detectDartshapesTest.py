import cv2
import numpy as np

# Load the image
image = cv2.imread('./Markers/dartDetect.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization to stretch the contrast
equalized = cv2.equalizeHist(gray)

# Blur the image to reduce noise
blurred = cv2.GaussianBlur(equalized, (5,5), 0)

# Perform edge detection
edged = cv2.Canny(blurred, 10, 250)

# Find contours in the image
cnts, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours
for c in cnts:
    # Approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)

    # Skip non-convex shapes
    if not cv2.isContourConvex(approx):
        continue

    # Compute the bounding rectangle of the shape
    (x, y, w, h) = cv2.boundingRect(approx)

    # Check if the shape is a dart
    if len(approx) == 3 and w > 10 and h > 10:
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, "Dart", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

# Show the image
cv2.imshow("Image", equalized)
cv2.waitKey(0)
