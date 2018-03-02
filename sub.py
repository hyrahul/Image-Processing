import numpy as np
import cv2
import cv

cap = cv2.VideoCapture('/root/Desktop/Input/Night/New folder/MB Ground Floor New_Camera11_MB Ground Floor New_20170919191600_20170919191859_2803563.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.BackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
 
    cv2.namedWindow('Frame a',cv2.WINDOW_OPENGL)
    cv2.namedWindow('Frame b',cv2.WINDOW_OPENGL)
    cv2.resizeWindow('Frame a', 600,600)
    cv2.resizeWindow('Frame b', 600,600)
    cv2.imshow('Frame a',fgmask)
    cv2.imshow('Frame b',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

