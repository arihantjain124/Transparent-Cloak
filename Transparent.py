from PIL import Image
from skimage import data,filters
import cv2
import numpy as np
from matplotlib import pyplot as plt

def empty(a):
    pass
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
cv2.namedWindow("ColorSelection")
cv2.resizeWindow("ColorSelection",720,310)
cv2.createTrackbar("Hue Min","ColorSelection",0,179,empty)
cv2.createTrackbar("Hue Max","ColorSelection",179,179,empty)
cv2.createTrackbar("Sat Min","ColorSelection",149,255,empty)
cv2.createTrackbar("Sat Max","ColorSelection",255,255,empty)
cv2.createTrackbar("Val Min","ColorSelection",61,255,empty)
cv2.createTrackbar("Val Max","ColorSelection",141,255,empty)

success ,imgbehind =cap.read()

while True:
    success ,img =cap.read()
    imgout=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min", "ColorSelection")
    h_max=cv2.getTrackbarPos("Hue Max", "ColorSelection")
    s_min=cv2.getTrackbarPos("Sat Min", "ColorSelection")
    s_max=cv2.getTrackbarPos("Sat Max", "ColorSelection")
    v_min=cv2.getTrackbarPos("Val Min", "ColorSelection")
    v_max=cv2.getTrackbarPos("Val Max", "ColorSelection")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgout,lower,upper)
    imask=np.invert(mask)
    img1=cv2.bitwise_and(img,img,mask=imask)
    img2=cv2.bitwise_and(imgbehind,imgbehind,mask=mask)
    imgfinal=cv2.addWeighted(img1,1.0,img2,1.0,0)
    cv2.imshow("Transparent",imgfinal)
    cv2.imshow("Live",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cv2.waitKey(0)
