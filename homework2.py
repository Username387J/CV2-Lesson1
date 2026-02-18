import cv2
greyimage=cv2.imread("flower.jpeg",0)
cv2.imshow("GreyScale Image",greyimage)

cv2.waitKey(0)
cv2.destroyAllWindows()