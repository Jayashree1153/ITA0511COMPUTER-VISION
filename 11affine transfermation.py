import cv2
import numpy as np
img = cv2.imread("D:\Pictures\my vision.jpg")
rows,cols,_ = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
result = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Affine Transform",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
