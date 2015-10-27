# -*- coding: utf-8 -*-
import os
import cv2

def getImgFileNames(folder):
    for nextfolder in os.listdir(folder):
        for f in os.listdir(folder + nextfolder)[1:]:
            fileName = folder + nextfolder + '/' + f
            yield fileName
            
def getFileName(outFolder, fileNum):
    return outFolder + 'iris_' + str(fileNum) + '.jpg'
    
def saveImage(img, outFolder, fileNum):
    fileName = getFileName(outFolder, fileNum)
    cv2.imwrite(fileName,img)