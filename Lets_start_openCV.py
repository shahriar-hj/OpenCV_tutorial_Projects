import cv2
import random

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
cv2.waitKey(1000)
cv2.destroyAllWindows()

# Image representation in BGR format not RGB :)
print(img)
print(type(img))
# number of height and width
print(img.shape)
# print  row of Image
print(img[150][15:128])

# manipulate image WITH RANDOM COLOR
for i in range(300):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
cv2.imshow(' Im show ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Copy and paste part of image
tag = img[300:400, 100:200]
img[100:200, 300:400] = tag
cv2.imshow(' replace Im show ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
