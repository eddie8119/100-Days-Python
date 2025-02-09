import numpy as np
import cv2


img = np.zeros((300, 300, 3), np.uint8)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 5)
cv2.rectangle(img, (0, 0), (100, 100), (0, 255, 0), 5)
cv2.circle(img, (100, 100), 50, (0, 0, 255), 5)
cv2.putText(img, "Hello World", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 5)

cv2.imshow("image", img)
cv2.waitKey(0)