import cv2 as cv
import numpy as np


img2 = cv.imread('park.jpg')
img= cv.resize(img2, (500,500), interpolation=cv.INTER_CUBIC )
cv.imshow('CAT', img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# thresholding is binarisation of image. image is wither 0 or 255. take an img and take a thresholding value and compare it. 
#  if the pixel intesnity is lower than the threshold value, image s binarised to 0 ie black
# if the pixel intensity is greater than the threshold value image is binarised to 255 ie white 

#  simple thresholding 

threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow('simple thresholded', thresh)

# inverse threshold image 
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded', thresh_inv)
# all the black parts of the img will change to white and vice versa 

# adoptive thresholding 
# it lets the computer to decide the optimal threshold value by its own 
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11, 3)
cv.imshow('adaptive Thresholding', adaptive_thresh)

# we have defined a kernal size ie 11*11, it computes the mean, and finds the optimal threshold value, and then it continues to slide to img and calculate
# in gaussian, the difference from mean is first it applies a weight to the pixel value, and then compute the mean across those pixels. 

cv.waitKey(0)