import cv2 as cv
import numpy as np

img2 = cv.imread('Park.jpg')
img= cv.resize(img2,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Park', img)

#methods of blurring
##a karnal/window is something that is drawn over an img. window has a size called karnal size that no of rows and column for ex. 3*3
##blur is applied in the middle pixel as a result of pixel around it. 

#1. averaging 
##a karnal window is defined over a specific part of the img. This window will compute the pixel intensity
##  the new pixel intensity of the middle region will be the evarge of pixel intensity of the surrounding pixel intensities. and this process happens throughout the image 

average= cv.blur(img, (3,3))
cv.imshow('average blur', average)
## highr karnal size we decide more blur is the image for example (7,7)
average2= cv.blur(img, (7,7))
cv.imshow('average blurrrr', average2)

#2.gausian blur 
##similar to averaging. but instead of cimputing the average 
##all surrounding pixels are given a pixel weight. average of products of those weights give the value of the centre. lesser blurr but the blur is more natural 

gauss= cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gaussian blur', gauss)

#3. Median blur
## it is averaging but rather than finding the average of pixel intensity of surrounding points it finds the median of the surrounding pixel . 
## more eefective in reducing noise as compared to other methods. used in advanced CV

Median= cv.medianBlur(img, 3)
cv.imshow('median blur', Median)

#4. Bilateral Blurring
##most effective  . bilateral applies blurring but retains the edges in the image 

bilateral= cv.bilateralFilter(img, 5, 25, 25)

#sigmaspace= larger value og sigma spacing pixel of one region will influence the computaion of the farther region too
cv.imshow('bilateral', bilateral)

 
cv.waitKey(0)