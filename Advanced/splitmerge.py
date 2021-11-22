import cv2 as cv
import numpy as np

img2 = cv.imread('Park.jpg')
img = cv.resize(img2, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', img)

#create a balnk image
blank= np.zeros(img.shape[:2], dtype='uint8')
#taking the image and split it into 3 color channels 

b,g,r = cv.split(img)

blue= cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red= cv.merge([blank,blank,r])


cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#regions where it is lighter there is more pixel value 
#regions where it is dareker there is less pixel value 

#after printing it shape of original image, 3 represents 3 color channels (bgr)
#in BGR shape of component is 1, shape of this image is grayscale

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)