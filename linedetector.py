import cv2
from gopigo import *


cap = cv2.VideoCapture(0)

black = [0, 0, 0]


while True:
    ret, frame = cap.read()

    detect_img = cv2.resize(frame, (3, 3))

    left_detect = frame[0][0] == black or frame[1][0] == black or frame[2][0] == black
    right_detect = frame[0][1] == black or frame[1][1] == black or frame[2][1] == black
    straight_detect = frame[0][2] == black or frame[1][2] == black or frame[2][2] == black

    if left_detect:
        left()
        time.sleep(1)
    elif right_detect:
        right()
        time.sleep(1)
    elif straight_detect:
        fwd()
        time.sleep(1)
    else:
        stop()
        break



