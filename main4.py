import cv2

img=cv2.imread("picachu.png")
cv2.imshow("Original Image",img)

B,G,R=cv2.split(img)

cv2.imshow("Blue Saturation Image",B)
cv2.imshow("Green Saturation Image",G)
cv2.imshow("Red Saturation Image",R)

cv2.waitKey(0)
cv2.destroyAllWindows()