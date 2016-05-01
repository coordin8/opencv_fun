import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # take each frame
    _, frame = cap.read()

    #convert to BGR to HSV
    hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )

    # define range of blue color in HSV
    lower_green = np.array( [ 75, 55, 55 ] )
    upper_green = np.array( [ 95, 255, 255 ] )

    # threshold the hsv image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    #bitwise "AND" mask the original image
    res = cv2.bitwise_and( frame, frame, mask = mask )

    cv2.imshow( 'frame',frame )
    cv2.imshow( 'mask', mask )
    cv2.imshow( 'res', res )

    k = cv2.waitKey(5) & 0xFF
    
    if k == 27:
        break


cv2.destroyAllWindows()
