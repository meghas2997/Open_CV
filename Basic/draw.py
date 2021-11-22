import cv2 as cv
import numpy as np

# 1. to make a blank image

blank =np.zeros((3, 3, 4), dtype='uint8')
print(blank)
cv.imshow('blank', blank)
# 2. paint image by certain color
blank[200:300,300:400]= 0,255,0
cv.imshow('green', blank)

# 3.draw a rectangle 
cv.rectangle(blank, (0,0), (250,500), (0,0,255), thickness=-1)
cv.imshow('rectangle', blank)

#4. draw a circle 
cv.circle(blank, (250, 250), 40, (255,0,0), thickness=cv.FILLED)
cv.imshow('circle', blank)

#5. draw a line 
cv.line(blank, (250,250), (300,400), (255,255,255), thickness=5)
cv.imshow('line', blank)

# 6. write a text
cv.putText(blank, 'hello my name is megha', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=1)
cv.imshow('text', blank)


cv.waitKey(0)
