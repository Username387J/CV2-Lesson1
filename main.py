import cv2
#2 is the version number
#open cv is open computer vision library
#imread-image read
# different modes(0=grayscale,1=color-transparency,-1=og)


image=cv2.imread("picachu.png",1)
#like root.title but root shows after 
cv2.imshow("output",image)

#Below 2 make sure it stays
cv2.waitKey(0)
cv2.destroyAllWindows()
