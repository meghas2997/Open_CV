import cv2 as cv
import numpy as np

img = cv.imread('Park.jpg')
cv.imshow('CAT', img)
print(img)
cv.waitKey(1)
