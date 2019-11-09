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
    
    cv2.imshow("Air Drum",img)
    if cv2.waitKey(10) == 27:
        cap.release()
        cv2.destroyAllWindows()
        break