# -*- coding: utf-8 -*-
import fileMngr as fm
import irisDetection as ID
import cv2

folderName = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS 395 Biometrics/hw2/2008-03-11_13/'
outFolder = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS 395 Biometrics/hw2/irisImages/'

def process(path, outFolder, imageNum):
    img = cv2.imread(path, 0)
    irisInner, irisOuter = ID.getIris(img)
    coloredIrisImg = ID.drawIris(img, irisInner, irisOuter)
    fm.saveImage(coloredIrisImg, outFolder, imageNum)

imgIndex = 0
for fileName in fm.getImgFileNames(folderName):
    process(fileName, outFolder, imgIndex)
    imgIndex += 1