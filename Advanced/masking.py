import cv2 as cv
import numpy as np


img2 = cv.imread('CAT.jpg')
img= cv.resize(img2, (500,500), interpolation=cv.INTER_CUBIC )
cv.imshow('CAT', img)

# masking allows us to focus on certain part of image. 
# if we are interested in focussing on the faces in a image 

blank= np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# dimensions of the mask has to be of same size as of the image otherwise it's going to fail

# mask= cv.circle(blank, (img.shape[1]//2 +100, img.shape[0]//2+ 45), 100, 255, -1)
circle= cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2),200 , 255, -1)
rectangle= cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

#weird shape
weird_shape= cv.bitwise_and(circle, rectangle)
cv.imshow('weird_shape', weird_shape)

# cv.imshow('mask',mask)

#masked image
masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('masked image', masked)








cv.waitKey(0)
