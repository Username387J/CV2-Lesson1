import cv2

image=cv2.imread("flower.jpeg")
cv2.imshow("Original Image",image)

B,G,R=cv2.split(image)

cv2.imshow("Blue Saturation Image",B)
cv2.imshow("Green Saturation Image",G)
cv2.imshow("Red Saturation Image",R)

cv2.waitKey(0)
cv2.destroyAllWindows()