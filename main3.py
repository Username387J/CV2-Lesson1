import cv2
import os

greyimg=cv2.imread("picachu.png",0)
cv2.imshow("Activity 3",greyimg)

path="/Users/joshdi/Documents/Jetlearn/OpenCV/Lesson1(Pull item from component)"
#chdir means change directory and it sets the directory to the variable its assigned to
os.chdir(path)

cv2.imwrite("test1.png",greyimg)
print("Image Has Saved Succesfully")

cv2.waitKey(0)
cv2.destroyAllWindows()