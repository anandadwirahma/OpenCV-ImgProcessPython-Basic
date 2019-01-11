import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)
# (512,512,4) ->
    # 512,512 is width & height
    # 3 source image channel (the value are 1,3,4)
# npuint8 -> typedef

# Draw a diagonal blue line with thickness of 3 px
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3) 
# cv2.line -> for drawing rectangle
# format : cv2.rectangle(img,pt1,pt2,color,thickness,lineType, shift)
    #- img    : Source image
    #- pt1    : First point of the line segment (coordinate cartisius)
    #- pt2    : Second point of the line segment (coordinate cartisius)
    #- color  : Line color
    #- thickness : line thickness
    #- lineType  : cv.FILLED/cv.LINE_4/cv.LINE_8/cv.LINE_AA
    #- shift     : Number of fractional bits in the point coordinates.
 
cv2.imshow('Drawing Rectangle', img)


k = cv2.waitKey(0)
if k == 27:                                         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('q'):                                 # wait for 's' key to save and exit
    cv2.destroyAllWindows()