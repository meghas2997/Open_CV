import cv2 as cv
import numpy as np

blank= np.zeros((400,400), dtype='uint8')
rectangle= cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(),(200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise AND  --> Intersecting regions 
bitwise_and= cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)

#bitwise OR --> non intersecting and intersecting regions
bitwise_or= cv.bitwise_or(rectangle, circle)
cv.imshow('or', bitwise_or)

#bitwiseXOR --> non intersecting regions 
bitwise_xor= cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# bitwise NOT
# it doesnt return anything  it inverts binary color 

bitwise_not= cv.bitwise_not(rectangle)
bitwise_not1= cv.bitwise_not(circle)
cv.imshow('bitwise_not1', bitwise_not1)



cv.waitKey(0)