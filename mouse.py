import numpy as np
import cv2

#minima_HSV=(130,10,75)
#maxima_HSV=(160,40,130)
def nothing(x):
    pass

cv2.namedWindow('Mouse',4)

cv2.createTrackbar('MinH','Mouse',0,255,nothing)
cv2.createTrackbar('MaxH','Mouse',0,255,nothing)
cv2.createTrackbar('MinS','Mouse',0,255,nothing)
cv2.createTrackbar('MaxS','Mouse',0,255,nothing)
cv2.createTrackbar('MinV','Mouse',0,255,nothing)
cv2.createTrackbar('MaxV','Mouse',0,255,nothing)

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    minima=(cv2.getTrackbarPos('MinH','Mouse'),cv2.getTrackbarPos('MinS','Mouse'),cv2.getTrackbarPos('MinV','Mouse'))
    maxima=(cv2.getTrackbarPos('MaxH','Mouse'),cv2.getTrackbarPos('MaxS','Mouse'),cv2.getTrackbarPos('MaxV','Mouse'))
    mask=cv2.inRange(hsv,minima,maxima)
    mask=cv2.flip(mask,1)

    mask=cv2.medianBlur(mask,5)
    cv2.imshow('Task Accomplished',mask)
    cv2.waitKey(1)
    
cv2.destroyAllWindows()    
    
