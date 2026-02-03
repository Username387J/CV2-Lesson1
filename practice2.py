import cv2
import os

flowerimg=cv2.imread("flower.jpeg",0)
cv2.imshow("Save flower img",flowerimg)


path="/Users/joshdi/Documents/Jetlearn/OpenCV/Lesson1(Pull item from component)"

os.chdir(path)
cv2.imwrite("flowertest1.jpeg",flowerimg)

print("Image Saved Succesfully")
cv2.waitKey(0)
cv2.destroyAllWindows()