import cv2 as  cv
import matplotlib as plt

#matplotlib is a library used for making plots 

img=cv.imread('Cat.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show() 

#BGR to grascale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
## grayscale image shows distribution of pixel intensity at particular locations of your image

#BGR to HSV(huge centuration value)
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to LAB(L*a*b)
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB 
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

## we can convert grayscale/hsv/lab to bgr, but we can't convert grayscale to hsv/lab directly 

#HSV to BGR 
hsv_bgr= cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

#BGR to lab
bgr_lab= cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('gdhg', bgr_lab)


cv.waitKey(0)
