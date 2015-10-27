# -*- coding: utf-8 -*-

import irisDetectionHelper as idh
import cv2

def getIris(img):
    iris = idh.findIris(img)
    roiForPupil, dstRowCol = idh.fromCircGetROI(img, iris)
    retval, roiForPupil = cv2.threshold(roiForPupil, 50, 255, cv2.THRESH_BINARY)
    pupil = idh.findPupil(roiForPupil)
    dstPupil = idh.translatedCircle(pupil, dstRowCol)
    return dstPupil, iris

def drawIris(img, pupil, iris):
    cImg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    cImg = idh.drawCircle(cImg, iris)
    cImg = idh.drawCircle(cImg, pupil)
    return cImg