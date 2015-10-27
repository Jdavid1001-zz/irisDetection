# -*- coding: utf-8 -*-

#import irisDetectionHelper as idh
import cv2
import cv2.cv as cv
import numpy as np
import os

filename = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS\ 395\ Biometrics/hw2/2008-03-11_13/04233/04233d1712.tiff'

def process(path):
    img = cv2.imread(path,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(cimg,cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=30,maxRadius=150)

    circles = np.around(circles)
    
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

process(filename)


"""
folder = 'C:/Users/Joel/Desktop/2008-03-11_13/2008-03-11_13/'
for nextfolder in os.listdir(folder):
    for f in os.listdir(folder + nextfolder)[1:]:
        process(folder+nextfolder+'/'+f)
        
"""