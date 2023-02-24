import cv2 as cv

img = cv.imread('openCV_Tutorial/imgs/gato.png')


def rescaleFrame(frame, scale=0.30):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)

cv.imshow('Cat', resized_image)
# Converting to grayscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#Blur image
blur = cv.GaussianBlur(resized_image,(5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edges', canny)

# Dilatando la imagen
dilated = cv.dilate(canny, (7,7), iterations=1)
#cv.imshow('Dilated', dilated)

# Erosion
eroded = cv.erode(dilated, (7,7), iterations=1)
#cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#cv.imshow('Resized', resized)

# Cropping
cropped = resized_image[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)