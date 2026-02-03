import cv2

greyimg=cv2.imread("picachu.png",0)
cv2.imshow("Activity 2",greyimg)


cv2.waitKey(0)
cv2.destroyAllWindows()