import cv2

img = cv2.imread('assets/logo.png', -1)
# resize image in specific resize
img_resize_inspect = cv2.resize(img, (200, 200))
# resize image in relative Size
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# Lets rotate our image to 90 degree CounterClock
im_rotate = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

# lets save image to
cv2.imwrite('new_rotate.png', img_half)

cv2.imshow('Coffee Logo', img)
cv2.imshow('Coffee Logo in half', img_half)
cv2.imshow("our logo rotated", im_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
