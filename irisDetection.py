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
    
processFile(filename)