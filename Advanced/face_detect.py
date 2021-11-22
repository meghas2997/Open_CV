import cv2 as cv

img = cv.imread('group1.jpeg')
cv.imshow('lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect= haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors =1)

print(f'Number of faces found= {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
cv.imshow('detected face', img)

#  haar cascades are not most effective because they are prone to more noise

cv.waitKey(0)