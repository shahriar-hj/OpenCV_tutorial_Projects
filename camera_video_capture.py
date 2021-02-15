import numpy as np
import cv2

# use webcam capture
cap = cv2.VideoCapture(0)
# use .mp4 file
# cap = cv2.VideoCapture('Filename')

# keep the capturing on
while True:
    ret, frame = cap.read()
    # cap.read value 3 is width
    width = int(cap.get(3))
    # cap.read Value 4 is height
    height = int(cap.get(4))
    # make frame for 4 image
    image = np.zeros(frame.shape, np.uint8)
    # make the whole Image smaller in size
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # indexing each smaller image to be in whole frame
    image[:height // 2, :width // 2] = smaller_frame
    image[height // 2:, :width // 2] = smaller_frame
    image[:height // 2, width // 2:] = smaller_frame
    image[height // 2:, width // 2:] = smaller_frame

    cv2.imshow('Frame ', image)
# how to quit by pressing "Q" on keyboard
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
