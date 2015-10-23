# -*- coding: utf-8 -*-
import cv2
import numpy as np

def getBinaryEdgesFromFile(fileName):
    img = cv2.imread(fileName, 0)
    binaryEdgeImg = cv2.Canny(img, 0, 255)
    return binaryEdgeImg

def getArrayOfEdges(binaryEdgeImg):
    edgesXY = np.where(binaryEdgeImg > 0)
    return zip(*edgesXY)
    
def getAcc(binaryEdgeImg):
    (rows, cols) = binaryEdgeImg.shape
    maxR = int(np.sqrt(rows**2 + cols**2)) + 1
    return np.zeros((rows, cols, maxR), dtype=np.uint16)
    
def processAcc(emptyAccumulator, binaryEdgeImg, edges):
    (rows, cols) = binaryEdgeImg.shape
    for r in xrange(rows):
        for c in xrange(cols):
            for edge in edges:
                radius = int(np.linalg.norm(np.array([r, c]) - np.array(edge)))
                emptyAccumulator[r][c][radius] += 1
                
                
"""
def makeCircles():
def getCircles(maxR):
    circles = None
    fileNameCircles, fileMaxR = 
    if circles not saved: 
        circles = makeCircles(maxR)
        pickle.save(circles)
    else:
        circles = pickle.load(circles)
    return circles

def removeBorders(img, maxR):
    rows, cols = img.shape()
    zeroedMatrix = numpy.zeros((rows, cols), dtype = same as image)
    radiusVector = [sin(45)maxR, cos(45)maxR]
    upperLeftCorner = [0,0] + radiusVector
    lowerRightCorner = [rows, cols] - radiusVector
    roi = regionOfInterest where x goes from 
        upperLeftCorner[0] to lowerRightCorner[0], 
        and y goes from upperLeftCorner[1] to lowerRightCorner[1]
    return zeroedMatrix + roi

def prepareImg(fileName, maxR):
    img = blackWhiteImage
    edgeImg = cannyEdgeDetect
    return removeBorders(img, maxR)
    
    
def houghCircle(img, minR, maxR, edgesArr, circles, acc):
    for center in edgesArr:
        for r in xrange(minR:maxR):
            acc += circleMatrix(circles, r, center)
        
    return getMaxCenterR(acc)
"""





