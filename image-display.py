import numpy as np
import cv2

img = cv2.imread('img/bags.jpg', 0)                 # Open image and Greyscale mode
cv2.namedWindow('image', cv2.WINDOW_NORMAL)         # Display in size window normal mode
cv2.imshow('image', img)                            # Display image
k = cv2.waitKey(0)
if k == 27:                                         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):                                 # wait for 's' key to save and exit
    cv2.imwrite('img/bags_greyscale.jpg', img)
    cv2.destroyAllWindows()