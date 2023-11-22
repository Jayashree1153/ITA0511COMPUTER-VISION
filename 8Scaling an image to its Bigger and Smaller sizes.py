import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
img = cv2.imread("D:\Pictures\my vision.jpg")
img = cv2.resize(img,(400,800))
cv2.imshow("image",img)
cv2.waitKey(0)
