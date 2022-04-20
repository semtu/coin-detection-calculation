#import required modules
import cv2
import numpy as np
import math

#read coin image
coins = cv2.imread(r'C:/Users/personal/Documents/openCV/matt/coins.jpg', 1)
#for j in range(50,100):
# defining minimal and maximal radius, specified to the coins.jpg
min_r = 24
max_r = 34

gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(
    img,  # source image
    cv2.HOUGH_GRADIENT,  # type of detection
    1,
    40,
    param1=80,
    param2=31,
    minRadius=min_r*2,  # minimal radius
    maxRadius=max_r*2,  # max radius
)

coins_copy = coins.copy()
i=0
for detected_circle in circles[0]:
    i+=1
    x_coor, y_coor, detected_radius = detected_circle
    font = cv2.FONT_HERSHEY_SIMPLEX
    coins_detected = cv2.putText(coins_copy, '#{}'.format(i), (int(x_coor-25), int(y_coor)), font, 1, (255, 0, 0), 3, cv2.LINE_AA)
    coins_detected = cv2.circle(coins_copy, (int(x_coor), int(y_coor)), int(detected_radius), (0, 0, 255), 1)

    print(f"circle {i} has a radius of {detected_radius}")
#     radiuses.append(detected_radius)
# score=0
# for radii in radiuses:
#     if radii<50:
#         score+=10
#     elif radii>60:
#         score+=25
#     else:
#         score+=5

# if score==80:
#     #print(j)
#     print('Good loop')

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image', coins_detected)
k = cv2.waitKey(0)
cv2.destroyAllWindows()