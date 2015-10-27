# -*- coding: utf-8 -*-

import irisDetectionHelper as idh
import cv2
import cv2.cv as cv
import numpy as np
import os

filename = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS\ 395\ Biometrics/hw2/2008-03-11_13/04233/04233d1712.tiff'

def getIris(img):
    iris = idh.findIris(img)
    roiForPupil, squareRowCol = idh.fromCircGetROI(img, iris)
    pupil = idh.findPupil(roiForPupil)
    return pupil, iris

def drawIris(img, pupil, iris):
    cImg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    cImg = idh.drawCircle(cImg, iris)
    cImg = idh.drawCircle(cImg, pupil)
    
def getFileName(outFolder, fileNum):
    return 'iris_' + str(fileNum) + '.jpg'
    
def saveImage(img, outFolder, fileNum):
    fileName = getFileName(outFolder, fileNum)
    

def process(path, outFolder):
    img = cv2.imread(filename, 0)
    irisInner, irisOuter = getIris(img)
    coloredIrisImg = drawIris(img, irisInner, irisOuter)
    saveImage(coloredIrisImg, outFolder)

process(filename)


"""
folder = 'C:/Users/Joel/Desktop/2008-03-11_13/2008-03-11_13/'
currentFile = 0
for nextfolder in os.listdir(folder):
    for f in os.listdir(folder + nextfolder)[1:]:
        process(folder+nextfolder+'/'+f, currentFile)
        currentFile += 1
        
"""