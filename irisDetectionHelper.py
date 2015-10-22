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