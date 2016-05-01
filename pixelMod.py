import cv2
import numpy as np

img = cv2.imread('nature.jpg')

rows, cols, colors = img.shape


for x in range(cols):
    for y in range(rows):
        img[x,y] *= 1.2


cv2.imshow( 'image', img )



cv2.waitKey(0)
