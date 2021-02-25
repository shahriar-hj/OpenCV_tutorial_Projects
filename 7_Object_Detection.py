import cv2
import numpy as np

img = cv2.imread('assets/soccer_practice.jpg', 0)
template_ball = cv2.imread('assets/ball.png', 0)
template_shoes = cv2.imread('assets/shoe.png', 0)
h, w = template_ball.shape
h1, w1 = template_shoes.shape

# algoritm for object Detection
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template_ball, method)
    result2 = cv2.matchTemplate(img2, template_shoes, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    min_val_1, max_val_1, min_loc_1, max_loc_1 = cv2.minMaxLoc(result2)
    print(min_loc, max_loc)
    print(min_loc_1, max_loc_1)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
        location_1 = min_loc_1
    else:
        location = max_loc
        location_1 = max_loc_1

    bottom_right = (location[0] + w, location[1] + h)
    bottom_right_1 = (location_1[0] + w1, location_1[1] + h1)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.rectangle(img2, location_1, bottom_right_1, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
