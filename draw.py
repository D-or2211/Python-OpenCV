import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
img = cv.imread('openCV_Tutorial/imgs/gato.png')
#cv.imshow('cat', img)
cv.imshow('Blank Image', blank)

# pintar la imagen de un color en concreto
# color verde
#blank[200:300, 300:400] = 0,0,255

# dibujar rectangulo
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#Otra forma de rellenar el rectangulo
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness=-1)
#cv.imshow('Rectangle', blank)

# Dibujar un circulo
#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
#cv.imshow('Circle', blank)

#Dibujar una linea
#cv.line(blank, (100,250),(300,400),(255,255,255), thickness=3)
#cv.imshow('Linea', blank)

# TEXTO EN LA IMAGEN
cv.putText(blank, 'Hola jotos .i.', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),thickness=2)
cv.imshow('texto', blank)
cv.waitKey(0)