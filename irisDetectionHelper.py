# -*- coding: utf-8 -*-
import cv2
import cv2.cv as cv
import numpy as np

def translatedCircle(circleArrParams, dstRowCol):
    r = circleArrParams[2]
    relativeRow = circleArrParams[1]
    relativeCol = circleArrParams[0]
    newRow = dstRowCol[0] + relativeRow
    newCol = dstRowCol[1] + relativeCol
    return [newCol, newRow, r]

def findIris(img):
    iris = findCircle(img, 60, 150, 80)
    return iris

def findPupil(img):
    pupil = findCircle(img, 10, 120, 10)
    return pupil

def findCircle(img,circleMinRadius,circleMaxRadius, minThreshold):
    circles = None
    minRadiusOriginal = circleMinRadius
    minThreshOriginal = minThreshold
    reduceMinRadius = True
    reduceMinThreshold = False
    while circles is None:
        circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT, 1, 20,
                                   param1= 50,param2= minThreshold, 
                                   minRadius= circleMinRadius, maxRadius= circleMaxRadius)
        if reduceMinRadius:                                   
            circleMinRadius -= 5
        if reduceMinThreshold:
            minThreshold -= 5
        if (reduceMinRadius and reduceMinThreshold) and (circleMinRadius <= 0 or minThreshold <= 0):
            height, width = img.shape
            x = height/2
            y = width/2
            r = min([height, width]) /4
            return [int(i) for i in [x,y,r]]
        if circleMinRadius <= 0:
            reduceMinRadius = False
            reduceMinThreshold = True
            circleMinRadius = minRadiusOriginal
        if minThreshold <= 0:
            minThreshold = minThreshOriginal
            reduceMinRadius = True

    minRadius = 0                           
    for i in range(len(circles[0])):
        if circles[0][i][2] > minRadius:
            minRadius = circles[0][i][2]
            index = i
    
    return [int(i) for i in np.around(circles[0][index])]

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
    
