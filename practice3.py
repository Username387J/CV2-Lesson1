import cv2

flowerimg=cv2.imread("flower.jpeg")
cv2.imshow("Original Image",flowerimg)

B,G,R=cv2.split(flowerimg)
cv2.imshow("Blue Saturated Image",B)
cv2.imshow("Green Saturated Image",G)
cv2.imshow("Red Saturated Image",R)

cv2.waitKey(0)
cv2.destroyAllWindows()