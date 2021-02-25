import numpy as np
import cv2

img = cv2.imread('assets/pexels-gagan-kaur-1170659.jpg')

# resize image
img = cv2.resize(img, (0, 0), fx=0.15, fy=0.15)

# make it grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Corner detection algorithm
corners = cv2.goodFeaturesToTrack(gray, 100, 0.55, 10)

# convert them into int
corners = np.int0(corners)

# find corners and make circle shape for them
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Draw Lines between each corner
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
