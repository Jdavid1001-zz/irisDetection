# -*- coding: utf-8 -*-
import cv2
import cv2.cv as cv
import numpy as np

filename = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS 395 Biometrics/hw2/2008-03-11_13/04233/04233d1712.tiff'

img = cv2.imread(filename, 0)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
circles = cv2.HoughCircles(img, cv.CV_HOUGH_GRADIENT, 1, 30,
                            param1=50,param2=80,minRadius=30,maxRadius=150)

print circles

circles = np.around(circles)

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()