import cv2 as cv

img = cv.imread('Park.jpg')

def rescaleFrame(frame, scale=0.2):
    #images, videos, etc
    width= int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale )
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
img2= rescaleFrame(img)
cv.imshow('Park', img2)

# converting to grayscale
gray =cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

# blur 
blur = cv.GaussianBlur(img2, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade 
canny = cv.Canny(img2, 500, 575)
cv.imshow('canny edges', canny)

# dilating the image
dilated =cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated image', dilated)

# Eroding
eroded =cv.erode(dilated, (3,3), iterations=1)
cv.imshow('dilated image', eroded)

# Resize 
resized = cv.resize(img2, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resized)

# Cropping 
Cropped = img[50:200, 200:400]
cv.imshow('cropped', Cropped)



cv.waitKey(0)