import cv2
import numpy as np
from gopigo import *
import time


cap = cv2.VideoCapture(0)

black = np.array([0, 0, 0])


while True:
    ret, frame = cap.read()

    detect_img = cv2.resize(frame, (3, 3))

    left_detect = np.array_equal(detect_img[0][0], black) or np.array_equal(detect_img[1][0], black) or np.array_equal(detect_img[2][0], black)
    right_detect = np.array_equal(detect_img[0][1], black) or np.array_equal(detect_img[1][1], black) or np.array_equal(detect_img[2][1], black)
    straight_detect = np.array_equal(detect_img[0][2], black) or np.array_equal(detect_img[1][2], black) or np.array_equal(detect_img[2][2], black)

    if left_detect and not right_detect:
        left()
        time.sleep(1)
    elif right_detect and not left_detect:
        right()
        time.sleep(1)
    elif straight_detect:
        fwd()
        time.sleep(1)
    else:
        stop()
        break



