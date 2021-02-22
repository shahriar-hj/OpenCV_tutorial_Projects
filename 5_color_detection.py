import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    # convert color image to HSV measure
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_Blue = np.array([90, 50, 50])
    upper_Blue = np.array([130, 255, 255])

    # creat Mask for the part you need of Pic
    mask = cv2.inRange(hsv, lower_Blue, upper_Blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
