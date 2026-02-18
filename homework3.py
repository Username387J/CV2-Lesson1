import cv2
import os
greyedimage=cv2.imread("flower.jpeg",0)
cv2.imshow("Cloned Image",greyedimage)

path="/Users/joshdi/Documents/Jetlearn/OpenCV/Lesson1(Pull item from component)"
os.chdir(path)

cv2.imwrite("flowertest1.png",greyedimage)
print("Image Has Saved Sucessfully")

cv2.waitKey(0)
cv2.destroyAllWindows()
