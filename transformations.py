import cv2 as cv
import numpy as np
img = cv.imread('openCV_Tutorial/imgs/gato.png')

def rescaleFrame(frame, scale=0.30):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
img = rescaleFrame(img)

cv.imshow('Gato', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x ===> left
# -y ===> Up
# x ===> Right
# y ====> down

# I recommend you to play with this part of code where you 
translated = translate(img, -100, 100)
#cv.imshow('Translated', translated)

# ROTATION
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
#cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -90)
#cv.imshow('Rotated rotaded', rotated_rotated)

# RESIZING
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

# FLIPPING
# 0 voltea de forma vertical, 1 = de forma horizontal
# -1 ambas
flip = cv.flip(img, 0)
#cv.imshow('Fliiped', flip)

# CROPPING
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)