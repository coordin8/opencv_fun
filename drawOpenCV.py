import numpy as np
import cv2


# creating the zero matrix image
img = np.zeros( (512,512,3), np.uint8 )

# draw diagonal blue line with thickness of zero
cv2.line( img, (0,0), (511,511), (255,0,0),5)

# drawing green rectangle with thickness of 3
cv2.rectangle( img, (384,0), (510,128), (0,255,0), 3 )  

# drawing a circle
cv2.circle( img, (447,63),63, (0,0,255), -1 )

# draw blue ellipse with 180 degree swing
cv2.ellipse( img, (256,256), (100,50), 0,0, 180, 255, -1 )

# draw polygon... first create points then transform those into shape
pts = np.array( [[10,5],[20,30],[70,20], [50,10]], np.int32 )
pts = pts.reshape( (-1,1,2) )
cv2.polylines( img, [pts],True, (0,255,255) )



font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText( img,'OpenCV',(10,500), font, 4, (255,255,255),2, cv2.LINE_AA)


# show image
cv2.imshow( 'image',img )
cv2.waitKey(0)
cv2.destroyAllWindows()



