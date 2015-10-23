# -*- coding: utf-8 -*-

import irisDetectionHelper as idh
import cv2


filename = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS 395 Biometrics/hw2/2008-03-11_13/04233/04233d1712.tiff'

def processFile(fileName):
    binImgOfEdges = idh.getBinaryEdgesFromFile(fileName)
    cv2.imshow('image',binImgOfEdges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    arrOfEdges = idh.getArrayOfEdges(binImgOfEdges)
    zeroedAccumulator = idh.getAcc(binImgOfEdges)
    accumulator = idh.processAcc(zeroedAccumulator, binImgOfEdges, arrOfEdges)
    print accumulator
    
#processFile(filename)


"""
def processFile(fileName, minR, maxR, circles):
    img = idh.prepareImg(fileName, maxR)
    edgesArr = getArrayOfEdges(img)
    zeroedAccumulator = getAcc(img, minR, maxR)
    center, radius = houghCircle(img, minR, maxR, edgesArr, circles, zeroedAccumulator)
    return (center, radius)

def processFolder(folderName, minR, maxR):
    circles = idh.getCircles(maxR)
    for each file in Folder:
        processFile(fileName, minR, maxR, circles)
"""