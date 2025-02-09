import cv2
import numpy as np
import os

kernel = np.ones((5,5), np.uint8)

# 使用絕對路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "example.jpg")

img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (15,15), 10)
canny = cv2.Canny(img, 50, 150) 
dilate = cv2.dilate(canny, kernel, iterations=1)   


cv2.imshow("gray", gray)
cv2.imshow("blur", blur)
cv2.imshow("canny", canny)
cv2.imshow("dilate", dilate)
cv2.waitKey(0)