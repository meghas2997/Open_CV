import cv2 as cv
import numpy as np

img= cv.imread('CAT.jpg')
cv.imshow('CAT', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> Right 
# y --> down 
translated = translate (img, 100, 100)
cv.imshow('translated', translated)

# Rotation
def rotate(img, angle, rotPoint= None):
    (height,width) =img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotate', rotated)

# to rotate the rotated image 

rotated_rotated = rotate(rotated, -90)
cv.imshow('rotated rotated', rotated_rotated)

# Resize an image 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resize', resized)

# Flipping 
flip= cv.flip(img, -1)
cv.imshow('flip', flip)
# 0 --> vertically 
# 1 --> horizontally
# -1 --> both vertical and horizontal 

# cropping 
cropped= img[200:400, 300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)