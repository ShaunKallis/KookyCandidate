import numpy as np
import cv2
from PIL import Image



#this code makes the picture more blurry
src = cv2.imread("barackobama.jpg", cv2.IMREAD_UNCHANGED)
dst = cv2.GaussianBlur(src,(11,11),50)
cv2.imshow("GaussianBlur",np.hstack((src,dst)))
cv2.waitKey(0)




#this code make the greyscale of the picture
image = cv2.imread("barackobama.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("barackobama10.jpg", dst)
cv2.imwrite("barackobama20.jpg", image_gray)


#this code flips the picture
flipped_image = cv2.rotate(image, cv2.ROTATE_180)
cv2.imwrite("barackobama30.jpg", flipped_image)


#this code finds the edges of the picture
edges = cv2.Canny(image,100, 200)
cv2.imwrite("barackobama40.jpg", edges)


#read image
no_green = cv2.imread("barackobama.jpg")

print(no_green.shape)

# assign green channel to zeros
no_green[:,:,1] = np.zeros([no_green.shape[0], no_green.shape[1]])

#save image
cv2.imwrite("barackobama50.jpg",no_green) 
