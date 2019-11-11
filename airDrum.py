# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:03:45 2019

@author: Saransh
"""

import cv2

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    #Creating Sections on Web Camera
    cv2.rectangle(img, pt1=(25, 75), pt2=(175, 225), color=(255, 0, 0), thickness=2)
    cv2.rectangle(img, pt1=(225, 250), pt2=(375, 400), color=(0, 225, 0), thickness=2)
    cv2.rectangle(img, pt1=(450, 75), pt2=(600, 225), color=(0, 0, 255), thickness=2)
    
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #Range of blue Color
    blue_lower = np.array([99,115,150],np.uint8)
    blue_upper = np.array([110,255,255],np.uint8)
    blue = cv2.inRange(hsv,blue_lower,blue_upper)
    
    kernal = np.ones((5,5),"uint8")
    blue = cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(img,img,mask=blue)
    (contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
    
    cv2.imshow("Air Drum",img)
    if cv2.waitKey(10) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
