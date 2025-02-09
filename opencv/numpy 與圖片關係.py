import numpy as np
import cv2

# numpy 陣列
img = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        img[row][col] = [255, 0, 0]


# 切片
newImg =img[:100, :200] = 0


cv2.imshow("image", img)
cv2.imshow("newImg", newImg)
cv2.waitKey(0)