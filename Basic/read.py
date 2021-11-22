import cv2 as cv

img = cv.imread('CAT.jpg')

cv.imshow('CAT', img)

def rescaleFrame(frame, scale=0.2):
    #images, videos, etc
    width= int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale )
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image= rescaleFrame(img)
cv.imshow('cat', resized_image)

def changeRes(width, height):
    #Live videos 
    capture.set(3, height)
    capture.set(4, width)

#Video read
capture = cv.VideoCapture('dog.gif')
while True:
    istrue, frame =capture.read()
    frame_resized = rescaleFrame(frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
       break
    cv.imshow('Video',frame_resized)
capture.release()
cv.destroyAllWindows()
