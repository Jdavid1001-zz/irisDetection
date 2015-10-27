# -*- coding: utf-8 -*-
import cv2
import cv2.cv as cv
import numpy as np

def findIris(img):
    iris = findCircle(img,60,150)
    return iris

def findPupil(img):
    pupil = findCircle(img,10,100)
    return pupil

def findCircle(img,circleMinRadius,circleMaxRadius):
    circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,20,
                               param1=50,param2=80,minRadius=circleMinRadius,maxRadius=circleMaxRadius)        
    minRadius = 0                           
    for i in range(len(circles[0])):
        if circles[0][i][2] > minRadius:
            minRadius = int(round(circles[0][i][2]))
            index = i
    
    return np.around(circles[0][index])

def drawCircle(coloredImg, circleArrParams):
    cv2.circle(coloredImg, (circleArrParams[0], circleArrParams[1]), 
               circleArrParams[2], (0, 255, 0), 2)
    return coloredImg

def fromCircGetROI(img, circleArrParams):
    r = circleArrParams[2]
    col0 = circleArrParams[0] - r
    row0 = circleArrParams[1] - r
    col1 = circleArrParams[0] + r
    row1 = circleArrParams[1] + r
    roi = img[row0:row1, col0:col1]
    return roi, (row0, col0)
    
