import cv2 as cv
import numpy as np

img = cv.imread('CAT.jpg')
cv.imshow('CAT', img)

#blank = np.zeros(img.shape, dtype = 'uint8')
blank = np.zeros(img.shape, dtype = 'uint8')
#blank.fill(150)
cv.imshow('blank', blank)


gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blur= cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny= cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)

ret, thresh = cv.threshold(gray , 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)


contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!') 

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours drawn', blank)

 #contours looks out at str element and returns to value
 # contours --- python list of all contours 
 # retr list essentially is mode to fine contours returns and finds the contours 
 # retr external returns external contours 
 #retr tree returns heirarchical contours 
 # chain approx none returns all the contours and simple takes all the points and compresses into to points only 
 

cv.waitKey(0)
