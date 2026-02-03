import cv2

flowerimg=cv2.imread("flower.jpeg",0)
cv2.imshow("Practice 1",flowerimg)

cv2.waitKey(0)
cv2.destroyAllWindows()