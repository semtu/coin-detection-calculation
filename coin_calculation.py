import cv2
import numpy as np
import math


def detect_coins():
    coins = cv2.imread(r'C:/Users/personal/Documents/openCV/matt/coins.jpg', 1)

    min_r = 24
    max_r = 34

    gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 40, param1=80, param2=31, minRadius=min_r*2, maxRadius=max_r*2 )

    coins_copy = coins.copy()
    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        coins_detected = cv2.circle(coins_copy, (int(x_coor), int(y_coor)), int(detected_radius), (0, 0, 255), 2)

    cv2.imwrite(r'C:/Users/personal/Documents/openCV/matt/coins_detected.jpg', coins_detected)
    return circles

def calculate_amount():
    cad_dict = {
        "5 CAD": {
            "value": 5,
            "radius": 21.2,
            "ratio": 1.1758,
            "count": 0,
        },
        "10 CAD": {
            "value": 10,
            "radius": 18.03,
            "ratio": 1,
            "count": 0,
        },
        "25 CAD": {
            "value": 25,
            "radius": 23.88,
            "ratio": 1.3245,
            "count": 0,
        },
    }

    circles = detect_coins()
    radius = list()
    coordinates = list()

    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        radius.append(detected_radius)
        coordinates.append([x_coor, y_coor])

    smallest = min(radius)
    tolerance = 0.088
    total_amount = 0

    coins_circled = cv2.imread(r'C:/Users/personal/Documents/openCV/matt/coins_detected.jpg', 1)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for coin in circles[0]:
        ratio_to_check = coin[2] / smallest
        coor_x = coin[0]
        coor_y = coin[1]
        for cad in cad_dict:
            value = cad_dict[cad]['value']
            if abs(ratio_to_check - cad_dict[cad]['ratio']) <= tolerance:
                cad_dict[cad]['count'] += 1
                total_amount += cad_dict[cad]['value']
                cv2.putText(coins_circled, '#'+str(value), (int(coor_x-30), int(coor_y+20)), font, 1.2, (0, 0, 255), 4)

    cv2.putText(coins_circled, 'Total Amount of Coins = #'+str(total_amount), (int(500), int(920)), font, 1.2, (0, 0, 255), 4)
    print(f"The total amount is {total_amount} CAD")
    for cad in cad_dict:
        pieces = cad_dict[cad]['count']
        print(f"{cad} = {pieces}x")

    cv2.namedWindow("image1", cv2.WINDOW_NORMAL)
    cv2.imshow('image1', coins_circled)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r'C:/Users/personal/Documents/openCV/matt/coins_calculated.jpg', coins_circled)


if __name__ == "__main__":
    calculate_amount()