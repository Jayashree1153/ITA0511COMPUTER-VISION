import cv2
path = "D:\Pictures\my vision.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
width = 650
height = 450
img_resized = cv2.resize(imgCanny, (width, height))
cv2.imshow('Original Image', img)
cv2.imshow("Img Canny",img_resized)
cv2.waitKey(0)
