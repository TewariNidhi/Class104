import cv2
import numpy as np
img = cv2.imread("butterfly.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#cv2.imshow("Display Image", gray_img)
print(img)
#cv2.waitKey(2000)
black = np.zeros([600, 600])
# f_row=black[1:2]
# f_col=black[:, 1:2]
black[200:400, 200:400]=255
cv2.imshow("black", black)
cv2.waitKey(0)