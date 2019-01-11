import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# (512,512,4) ->
    # 512,512 is width & height
    # 3 source image channel (the value are 1,3,4)
# npuint8 -> typedef

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5) 
# cv2.line -> for drawing line
# format : cv2.line(img,pt1,pt2,color,thickness,line, shift)
    #- img    : Source image
    #- pt1    : First point of the line segment (coordinate cartisius)
    #- pt2    : Second point of the line segment (coordinate cartisius)
    #- color  : Line color
    #- thickness : line thickness
    #- lineType  : cv.FILLED/cv.LINE_4/cv.LINE_8/cv.LINE_AA
    #-shift      : Number of fractional bits in the point coordinates.
 
cv2.imshow('Drawing Line', img)


k = cv2.waitKey(0)
if k == 27:                                         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('q'):                                 # wait for 's' key to save and exit
    cv2.destroyAllWindows()