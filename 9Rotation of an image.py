import cv2
path ="D:\Pictures\my vision.jpg"
src = cv2.imread(path)
image = cv2.rotate(src, cv2.ROTATE_180)
img = cv2.resize(image,(600,600))
cv2.imshow("image", img)
cv2.waitKey(0)

