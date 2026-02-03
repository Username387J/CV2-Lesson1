import cv2
#remember--import-->reading-->title+variable-->waiting 4approval to destry all windows
image=cv2.imread("flower.jpeg",1)
cv2.imshow("output",image)

cv2.waitKey(0)
cv2.destroyAllWindows()


