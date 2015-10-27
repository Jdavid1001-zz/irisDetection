# -*- coding: utf-8 -*-
import cv2
import cv2.cv as cv
import numpy as np
import irisDetectionHelper as idh

filename0 = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS 395 Biometrics/hw2/2008-03-11_13/04233/04233d1712.tiff'
filename1 = '/Users/JuanDa/Documents/Academics/2015-2016/Fall/EECS 395 Biometrics/hw2/2008-03-11_13/02463/02463d1927.tiff'

filenameArr = [filename0, filename1]

def showImg(img, title):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

for filename in filenameArr:
    img = cv2.imread(filename, 0)
    
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    iris = idh.findIris(img)
    cimg = idh.drawCircle(cimg, iris)



    pupil = idh.findPupil(roiForPupil)
    dstPupil = translatedCircle(pupil, dstRowCol)
    
    cimg = idh.drawCircle(cimg, dstPupil)
        
    showImg(cimg, 'detected circles')
